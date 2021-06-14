from django.db import models

# Create your models here.
class Name(models.Model):
    tipo = models.CharField(max_length=250)
    data_inicio = models.DateTimeField()
    data_fim = models.DateTimeField(blank=True, null=True)
    descricao = models.CharField(max_length=250)
    importante = models.BooleanField()

    

    def __str__(self):
        return str(self.id)
