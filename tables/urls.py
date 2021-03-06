from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('all/', views.get_all_tables, name="table-overview"),
    path('<int:table_id>/', views.get_table, name="table-data"),
    path('latest/<int:table_id>/',
         views.get_latest_snapshot, name="latest-table-data"),
    path('create/', views.create_table_snapshot, name="create-snapshot")
]
