from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .serializers import TransactionSerializer
from .models import TransactionModel

# Create your views here.


def index(request):

    return HttpResponse("Hello")

class TransactionView(generics.ListCreateAPIView):
    queryset = TransactionModel.objects.all()
    serializer_class = TransactionSerializer

    def get_queryset(self): 

        query_set = TransactionModel.objects.all()
        return query_set



