from django.contrib import admin
from django.urls import path
from . import views as company_views


urlpatterns = [
    path('company-details', company_views.company_details),
    path('careers', company_views.careers),
    path('portfolio', company_views.portfolio),
    path('teams', company_views.team)
]
