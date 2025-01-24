from django.urls import path
from . import views
from .views import TransactionView, AuthorizedUrlView

urlpatterns = [
    path("", views.index, name="Home Page"), 
    path("transact/",TransactionView.as_view(), name='transaction' ), 
    path("auth_url/", AuthorizedUrlView.as_view(), name="Generate Url view")
]
