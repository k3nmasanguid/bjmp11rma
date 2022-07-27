from django.urls import path
from rma import views

urlpatterns = [
   path('', views.home, name='home'),
]