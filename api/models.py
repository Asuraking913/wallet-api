from django.db import models

# Create your models here.

class TransactionModel(models.Model):
    id = models.CharField(max_length=255, primary_key=True, null=False, unique=True)
    reference = models.CharField(max_length=10, null=False, unique=True)
    amount = models.IntegerField()
    previous_balanec = models.IntegerField()
    new_balance = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.reference:
            self.reference = self.id[:10]
            
        super().save()
    