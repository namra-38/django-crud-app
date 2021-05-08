from django.urls import path
from . import views

urlpatterns = [
    path('list/',views.employes_list, name='employes_list'),
    path('<int:employe_id>/details/', views.employe_details, name='employe_details'),
    path('add/', views.add_employe, name='add_employe'),
    path('<int:employe_id>/edit/', views.edit_employe, name='edit_employe'),
    path('<int:employe_id>/delete/', views.detele_employe, name='detele_employe'),
]