from rest_framework import viewsets
from rest_framework.response import Response
from apps.products.models import MeasureUnit
from rest_framework import status

from apps.base.api import GeneralListApiView
from apps.products.api.serializers.general_serializers \
    import (MeasureUnitSerializer, CategoryProductSerializer,
            IndicatorSerializer)


class MeasureUnitListAPIView(viewsets.GenericViewSet):
    model = MeasureUnit
    serializer_class = MeasureUnitSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state = True)

    def list(self, request):
        """
            Retorna todas as unidades de medida do produto

            params.

            id -> PK da unidade de medida
            name -> nome da unidade de medida
        """
        data = self.get_queryset()
        data = self.get_serializer(data, many=True)
        return Response(data.data)



class CategoryProductListAPIView(viewsets.GenericViewSet):
    serializer_class = CategoryProductSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state = True)

    def get_object(self):
        return self.get_serializer().Meta.model.objects.filter(
            id=self.kwargs['pk'], state=True)

    def list(self, request):
        """
            Retorna todas as categorias de produto
        """
        data = self.get_queryset()
        data = self.get_serializer(data, many=True)
        return Response(data.data)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {'message':'Categoria registrada corretamente!'},
                status=status.HTTP_201_CREATED
            )
        return Response(
            {'message':'', 'error':serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )

    def update(self, request, pk=None):
        if self.get_object().exists():
            serializer = self.serializer_class(
                instance=self.get_object().get(), data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {'message':'Categoria atualizada corretamente!'},
                    status=status.HTTP_200_OK
                )
        return Response(
            {'message':'', 'error':serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )

    def destroy(self, request, pk=None):
        if self.get_object().exists():
            self.get_object().get().delete()
            return Response(
                {'message':'Categoria excluída corretamente!'},
                status=status.HTTP_200_OK
            )
        return Response(
            {'message':'', 'error':'Categoria não encontrada!'},
            status=status.HTTP_400_BAD_REQUEST
        )


class IndicatorListAPIView(viewsets.GenericViewSet):
    serializer_class = IndicatorSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state = True)

    def list(self, request):
        """
            Retorna todos os indicadores de produto
        """
        data = self.get_queryset()
        data = self.get_serializer(data, many=True)
        return Response(data.data)
