from rest_framework import serializers
from .models import CnabModel

class CnabSerializer(serializers.Serializer):
    type= serializers.IntegerField()
    date=serializers.DateField()
    value=serializers.CharField(max_length=10)
    cpf= serializers.CharField(max_length=11)
    card= serializers.CharField(max_length=12)
    hour=serializers.CharField(max_length=6)
    owner= serializers.CharField(max_length=14)
    establishment= serializers.CharField(max_length=19)

    def create(self, validated_data):
        data= CnabModel.objects.create(**validated_data)
        return data