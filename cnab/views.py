from django.shortcuts import render
from .models import FormCnab
from django.http import HttpResponse
from .serializers import CnabSerializer
from rest_framework.views import APIView, Response, status
import ipdb

def home(request):
    form = FormCnab()
    return render(request, "home.html", {"form": form})





def saveDb(request):

    to_save = open(request.POST['arquivo'], "r")
   
    every=to_save.readlines()
    for each in every:
        type= each[0]
        date= each[1:9]
        value= each[9:19]
        cpf= each[19:30]
        card=each[30:42]
        hour= each[42:48]
        owner= each[48:62]
        establishment= each[62:81]
        to_cnab={"type":type,"date":date,"value":value,"cpf":cpf,"card":card,"hour":hour,"owner":owner,"establishment":establishment}

        serializer=CnabSerializer(data=to_cnab)

        serializer.is_valid(raise_exception=True)
        serializer.save()


    return render(request, "success.html")

