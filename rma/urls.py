from django.urls import path
from rma import views

urlpatterns = [
   # loaded data to the home page
   path('', views.home, name='home'),
   path('personal-info-data/', views.personal_info_data, name='personal-info-data'),
   path('present-address-data/', views.present_address_data, name='present-address-data'),
   path('permanent-address-data/', views.permanent_address_data, name='permanent-address-data'),
   # launch modals home page
   path('personal-info/', views.personal_info, name='personal-info'),
   path('present-address/', views.present_address, name='present-address'),
   path('permanent-address/', views.permanent_address, name='permanent-address'),

   # loaded data to the background page
   path('background/', views.background, name='background'),
   path('spouse-data/', views.spouse_data, name='spouse-data'),
   path('father-data/', views.father_data, name='father-data'),
   path('mother-data/', views.mother_data, name='mother-data'),

   # launch modals background page
   path('spouse/', views.spouse, name='spouse'),
   path('father/', views.father, name='father'),
   path('mother/', views.mother, name='mother'),
   
]