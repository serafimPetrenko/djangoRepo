from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name='home'),
   path("pharmacy", views.pharmacy_page, name='pharmacy'),
   path("pills", views.pills_page, name='pills'),
   path("info", views.info_page, name='info'),
]