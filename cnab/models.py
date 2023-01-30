from django.db import models

from django import forms

class FormCnab(models.Model):
    arquivo= models.FileField(upload_to="documents/")


class CnabModel(models.Model):
    type= models.IntegerField()
    date=models.DateField()
    value=models.CharField(max_length=10)
    cpf= models.CharField(max_length=11)
    card= models.CharField(max_length=12)
    hour=models.CharField(max_length=6)
    owner= models.CharField(max_length=14)
    establishment= models.CharField(max_length=19)
