from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class BaseModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=128,default='fulano')

class Meta:
    abstract = True

class Cundina(BaseModel):
    mes = models.IntegerField(blank = True, null = True, default = 1)
    totalRecaudar = models.IntegerField(blank = True, null = True, default = 100)
    cantidadParticipantes = models.IntegerField(blank = True, null = True, default = 12)

    def __str__(self):
        return self.mes
