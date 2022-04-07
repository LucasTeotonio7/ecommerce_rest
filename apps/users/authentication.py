from datetime import timedelta

from django.utils import timezone
from django.conf import settings

from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed


class ExpiringTokenAuthentication(TokenAuthentication):

    expired = False

    def expires_in(self, token):
        time_elapsed = timezone.now() - token.created
        return timedelta(
            seconds = settings.TOKEN_EXPIRED_AFTER_SECONDS) - time_elapsed

    def is_token_expired(self, token):
        return self.expires_in(token) < timedelta(seconds=0)

    def token_expire_handler(self, token):
        is_expired = self.is_token_expired(token)
        print(is_expired)
        if is_expired:
            expired = True
            user = token.user
            token.delete()
            token = self.get_model().objects.create(user = user)
            print('token expirado')

        return is_expired, token

    def authenticate_credentials(self, key):
        message, token, user = None, None, None
        try:
            token = self.get_model().objects.select_related('user').get(key = key)
            user = token.user
        except self.get_model().DoesNotExist:
            # raise AuthenticationFailed('Token Inválido.')
            message = 'Token Inválido'
            self.expired = True

        if token is not None:
            if not token.user.is_active:
                # raise AuthenticationFailed('Usuário não ativo ou eliminado.')
                message = 'Usuário não ativo ou eliminado.'

            is_expired = self.token_expire_handler(token)
            if is_expired:
                # raise AuthenticationFailed('Seu token foi expirado.')
                message = 'Seu token foi expirado.'

        return (user, token, message, self.expired)
