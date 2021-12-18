from datetime import datetime

from django.contrib.sessions.models import Session

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken

from apps.users.api.serializers import UserTokenSerializer

class Login(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        login_serializer = self.serializer_class(
            data = request.data, context = {'request':request})

        if login_serializer.is_valid():
            user = login_serializer.validated_data['user']
            if user.is_active:
                token,created = Token.objects.get_or_create(user = user)
                user_serializer = UserTokenSerializer(user)
                print(token, created, user_serializer.data)
                if created:
                    return Response({
                        'token': token.key,
                        'user': user_serializer.data,
                        'message':'inicio de sessão'
                    }, status = status.HTTP_201_CREATED)
                else:
                    # all_sessions = Session.objects.filter(expire_date__gte=datetime.now())
                    # if all_sessions.exists():
                    #     for session in all_sessions:
                    #         session_data = session.get_decoded()
                    #         if(user.id == int(session_data.get('_auth_user_id'))):
                    #             session.delete()
                    # token.delete()
                    # token = Token.objects.create(user = user)
                    # return Response({
                    #     'token': token.key,
                    #     'user': user_serializer.data,
                    #     'message':'inicio de sessão'
                    # }, status = status.HTTP_200_OK)

                    token.delete()
                    return Response(
                    {'error':'este usuário já possui uma sessão ativa'},
                    status = status.HTTP_409_CONFLICT)
            else:
                return Response(
                    {'error':'este usuário não pode iniciar a sessão'},
                    status = status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(
            {'message':'nome do usuário ou senha incorreto'},
            status = status.HTTP_400_BAD_REQUEST)


class Logout(APIView):

    def get(self, request, *args, **kwargs):
        try:
            token = request.GET.get('token')
            token = Token.objects.filter(key = token).first()

            if token:
                user = token.user

                all_sessions = Session.objects.filter(expire_date__gte=datetime.now())
                if all_sessions.exists():
                    for session in all_sessions:
                        session_data = session.get_decoded()
                        if(user.id == int(session_data.get('_auth_user_id'))):
                            session.delete()

                token.delete()

                session_message = 'sessões encerradas.'
                token_message = 'token excluído.'

                return Response({
                    'token_message': token_message,
                    'session_message': session_message
                }, status = status.HTTP_200_OK)

            return Response({
                'error':'Não encontrado um usuário com essas credenciais'
            }, status = status.HTTP_400_BAD_REQUEST)

        except:
            return Response({
                'error': 'Não foi encontrado um token na requisição'
            }, status= status.HTTP_409_CONFLICT)
