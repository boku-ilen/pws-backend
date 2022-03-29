from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('all/', views.get_all_tables, name="table-overview"),
]
