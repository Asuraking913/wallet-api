from django.urls import path
from . import views
from .views import TransactionView

urlpatterns = [
    path("", views.index, name="Home Page"), 
    path("transact/",TransactionView.as_view(), name='transaction' )
]
