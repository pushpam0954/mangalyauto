from django.urls import path

from . import views

urlpatterns = [

    path('', views.Home, name="Home"),
    path('about/', views.about, name="About"),
    path('Contactus/', views.Contactus,name="Contactus"),
    path('Automotive/', views.Automotive,name="Automotive"),
    path('Defence/', views.Defence,name="Defence"),
    path('Ancillary/', views.Ancillary,name="Ancillary"),
    path('Technology/', views.Technology,name="Technology"),
    path('Automotive/', views.Automotive,name="Automotive"),
    path('Base/', views.Base ,name="PRODUCT PORTFOLIO")





]
