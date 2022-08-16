from django.urls import path
from bjmpadmin import views

urlpatterns = [
   path('', views.bjmpadmin, name='bjmpadmin'),
   path('bjmpadmin-search/', views.bjmpadmin_search, name='bjmpadmin-search'),
   path('bjmpadmin-profile/<str:id>', views.bjmpadmin_profile, name='bjmpadmin-profile'),
]