from django.urls import path
from . import views

urlpatterns = [
    path('', views.Credit.as_view(), name='urlCredit'),
]