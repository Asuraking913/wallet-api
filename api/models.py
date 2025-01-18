from django.db import models
from uuid import uuid4

# Create your models here.


def generate_id():

    return uuid4().hex

class TransactionModel(models.Model):
    id = models.CharField(max_length=255, primary_key=True, null=False, unique=True, default=generate_id)
    reference = models.CharField(max_length=10, null=False, unique=True)
    amount = models.IntegerField()
    previous_balance = models.IntegerField()
    new_balance = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.reference:
            self.reference = self.id[:10]
            
        super().save()
    