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
   path('sibling-data/', views.sibling_data, name='sibling-data'),
   path('children-data/', views.children_data, name='children-data'),
   # launch modals background page
   path('spouse/', views.spouse, name='spouse'),
   path('father/', views.father, name='father'),
   path('mother/', views.mother, name='mother'),
   path('sibling/', views.sibling, name='sibling'),
   path('sibling-edit/<str:id>/', views.sibling_edit, name='sibling-edit'),
   path('sibling-delete/<str:id>/', views.sibling_delete, name='sibling-delete'),
   path('children/', views.children, name='children'),
   path('children-edit/<str:id>/', views.children_edit, name='children-edit'),
   path('children-delete/<str:id>/', views.children_delete, name='children-delete'),

   # loaded data to the education page
   path('education/', views.education, name='education'),
   path('primary-data/', views.primary_data, name='primary-data'),
   # launch modals education page
   path('primary/', views.primary, name='primary'),
   path('primary-delete/<str:id>/', views.primary_delete, name='primary-delete'),
]