from rest_framework import serializers
from .models import TransactionModel

class TransactionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TransactionModel
        fields = ["reference", "amount", "previous_balance", "new_balance"]

class AuthorizationUrlSerializer(serializers.Serializer):
    amount = serializers.FloatField()
    email = serializers.EmailField()
