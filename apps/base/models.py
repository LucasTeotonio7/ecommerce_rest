from django.db import models

# Create your models here.

class BaseModel(models.Model):

    #TODO: Define fields here
    id = models.AutoField(primary_key=True)
    state = models.BooleanField('Situação', default=True)
    created_date = models.DateField('Data de criação', auto_now=False, auto_now_add=True)
    modified_date = models.DateField('Data de modificação', auto_now=True, auto_now_add=False)
    deleted_date = models.DateField('Data de exclusão', auto_now=True, auto_now_add=False)

    class Meta:
        abstract = True
        verbose_name = 'Modelo Base'
        verbose_name_plural = 'Modelos Base'
