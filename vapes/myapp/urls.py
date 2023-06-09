from django.contrib import admin
from django.urls import path, include
from myapp import views

urlpatterns = [
    path("", views.index, name='index'),
    path("products", views.products, name='products'),
    path("about", views.about, name='about'),
    path("contact", views.contact, name='contact')
]
