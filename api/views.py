from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, status
from .serializers import TransactionSerializer
from .models import TransactionModel
from rest_framework import views
from rest_framework.response import Response
from .flutterwave import FlutterwaveService
from .serializers import AuthorizationUrlSerializer

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

        serializer = AuthorizationUrlSerializer(data = request.data)

        if serializer.is_valid():
            data = serializer.validated_data

            flutterwave = FlutterwaveService()
            response = flutterwave.initiate_transaction(data['amount'], data['email'])


            return Response({"msg" : "Sent Data", "data" : response}, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



