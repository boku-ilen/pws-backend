from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('unresolved/', views.get_unresolved_reports, name="unresolved-reports"),
    path('create/<str:text>/', views.create_report, name="create-report"),
    path('create/<str:text>/<str:email>/',
         views.create_report, name="create-report"),
    path('resolve/<int:report_id>/', views.resolve_report, name="resolve-report")
]
