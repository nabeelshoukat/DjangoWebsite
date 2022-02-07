from django.contrib import admin
from django.urls import path,include
from . import views



urlpatterns = [
    path("",views.indexmob),
    path("newsdetails/<id>", views.news_details)

]



