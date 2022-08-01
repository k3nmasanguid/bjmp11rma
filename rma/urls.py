from django.urls import path
from rma import views

urlpatterns = [
   path('', views.home, name='home'),
   # loaded data to the page
   path('personal-info-data/', views.personal_info_data, name='personal-info-data'),
   path('present-address-data/', views.present_address_data, name='present-address-data'),
   # launch modals
   path('personal-info/', views.personal_info, name='personal-info'),
   path('present-address/', views.present_address, name='present-address'),
]