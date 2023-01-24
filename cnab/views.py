from django.shortcuts import render
from .models import FormCnab
from django.http import HttpResponse
from .serializers import CnabSerializer
from rest_framework.views import APIView, Response, status
import ipdb

def home(request):
    form = FormCnab()
    return render(request, "home.html", {"form": form})


class SaveDb(APIView):
    def post(self, request):



def saveDb(request):

    to_save = open(request.POST['arquivo'], "r")
   
    for _ in to_save:
        data=to_save.readline()
        type= data[0]
        date= data[1:9]
        value= data[9:19]
        cpf= data[19:30]
        card=data[30:42]
        hour= data[42:48]
        owner= data[48:62]
        establishment= data[62:81]

        CnabSerializer(type=type,date=date,value=value,
        cpf=cpf,card=card,hour=hour, owner=owner, establishment=establishment)

        CnabSerializer.is_valid(raise_exception=True)
        CnabSerializer.save()


    return HttpResponse(to_save.readline())
    serializer= CnabSerializer()
     

    return HttpResponse(to_save.readline())
