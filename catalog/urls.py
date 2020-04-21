from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='catalog-home'),
    path('about/', views.about, name='catalog-about'),
    path('mission/', views.mission, name='catalog-mission'),
    path('booklist/', views.booklist, name='catalog-booklist'),
    path('checkout/', views.checkout, name='catalog-checkout'),
    path('register/', views.register, name='catalog-register'),
    path('registerSubmit/', views.registerSubmit, name='catalog-registerSubmit'),
]
