from django.shortcuts import render
from .models import FormCnab
from .serializers import CnabSerializer

from django.core.files.storage import FileSystemStorage

import unidecode
import re



def home(request):
    form = FormCnab()
    return render(request, "home.html", {"form": form})





def saveDb(request):
    fs= FileSystemStorage()
    doc= fs.save("cnab.txt", request.FILES["arquivo"])
    to_save = open(f"media/{doc}","r")
    
   
    every=to_save.readlines()
    to_return= []
    for each in every:
        type= each[0]
        date= each[1:9]
        value1= each[9:19]
        cpf= each[19:30]
        card=each[30:42]
        hour= each[42:48]
        owner= unidecode.unidecode(each[48:62])
        establishment1= each[62:81]

        establishment =re.sub(u'[^a-zA-Z0-9áéíóúÁÉÍÓÚâêîôÂÊÎÔãõÃÕçÇ: ]', '', establishment1)

        value= value1.lstrip('0')

        to_cnab={"type":type,"date":date,"value":value,"cpf":cpf,"card":card,"hour":hour,"owner":owner,"establishment":establishment}
       
        asset=True
        for each in to_return:
            try:
                if each["establishment"] == establishment:
                    if type == "2" or type == "3" or type =="9":
                        previous_balance= each["balance"]
                        each.update({"balance": int(previous_balance) - int(value)})
                        asset=False
                    else:
                        each.update({"balance": int(previous_balance) + int(value)})
                        asset=False
            except:
                pass
        if asset:
            to_return.append({"establishment": establishment, "balance": value})


        serializer=CnabSerializer(data=to_cnab)

        serializer.is_valid(raise_exception=True)
        serializer.save()
    
    


    return render(request, "success.html",{"to_return": to_return})

