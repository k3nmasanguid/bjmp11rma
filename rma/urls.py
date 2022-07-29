from django.urls import path
from rma import views

urlpatterns = [
   path('', views.home, name='home'),
   path('personal-info/', views.personal_info, name='personal-info'),
]