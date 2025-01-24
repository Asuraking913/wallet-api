from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .serializers import TransactionSerializer
from .models import TransactionModel
from rest_framework import views
from rest_framework.response import Response
from .flutterwave import FlutterwaveService

# Create your views here.


def index(request):

    return HttpResponse("Hello")

class TransactionView(generics.ListCreateAPIView):
    queryset = TransactionModel.objects.all()
    serializer_class = TransactionSerializer

    def get_queryset(self): 

        query_set = TransactionModel.objects.all()
        return query_set

class AuthorizedUrlView(views.APIView):

    def post(self, request):
        amount = request.data.get('amount')
        email = request.data.get('email')

        print(amount, flush=True)
        print(email, flush=True)

        flutterwave = FlutterwaveService()

        response = FlutterwaveService().initiate_transaction(amount, email)

        print(response, flush=True)

        return Response({"msg" : "Sent Data"})



