from django.urls import path
from bjmpadmin import views

urlpatterns = [
   path('', views.bjmpadmin, name='bjmpadmin'),
]