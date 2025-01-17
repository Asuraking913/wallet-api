from rest_framework import serializers
from .models import TransactionModel

class TransactionSerializer(serializers.ModelField):
    
    class Meta:
        model = TransactionModel
        fields = ["reference", "amount", "previoud_balance", "new_balance"]