from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .serializers import TransactionSerializer

# Create your views here.


def index(request):

    return HttpResponse("Hello")

class TransactionView(generics.ListCreateAPIView):
    serializer_class = TransactionSerializer


