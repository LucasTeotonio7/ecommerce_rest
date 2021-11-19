from django.db import models
from django.db.models.fields import NullBooleanField
from simple_history.models import HistoricalRecords

from apps.base.models import BaseModel
# Create your models here.

class MeasureUnit(BaseModel):

    # TODO: Define fields here
    description = models.CharField("Descrição", max_length=50, blank=False, null=False, unique=True)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = 'Unidade de Medida'
        verbose_name_plural = 'Unidades de Medida'

    def __str__(self):
        return self.description


class CategoryProduct(BaseModel):

    # TODO: Define fields here
    description = models.CharField("Descrição", max_length=50, blank=False, null=False, unique=True)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = "Categoria de Produto"
        verbose_name_plural = "Categorias de Produto"

    def __str__(self):
        return self.description

class Indicator(BaseModel):

    # TODO: Define fields here
    discount_value = models.PositiveSmallIntegerField(default=0)
    category_product = models.ForeignKey(CategoryProduct, verbose_name="indicador de oferta", on_delete=models.CASCADE)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = "Indicador de Oferta"
        verbose_name_plural = "Indicadores de Ofertas"

    def __str__(self):
        return f'oferta da categoria{self.category_product} : {self.discount_value}%'

class Product(BaseModel):

     # TODO: Define fields here
    name = models.CharField('Nome do Produto', max_length=150, unique=True, blank=False, null=False)
    description = models.TextField('Descrição do Produto', blank=False, null=False)
    image = models.ImageField("Imagem do Produto", upload_to="products/", blank=True, null=True)
    measure_unit = models.ForeignKey(
        MeasureUnit, verbose_name="unidade de medida",
        on_delete=models.CASCADE, null=True
    )
    category_product = models.ForeignKey(
        CategoryProduct, verbose_name="Categoria do produto",
        on_delete=models.CASCADE, null=True
    )
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"

    def __str__(self):
        return self.name
