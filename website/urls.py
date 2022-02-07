from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),

    path("", views.index, name="home"),
    path('mobile/',include('mobile.urls')),
    path("about", views.about, name="about"),
    path("contact", views.contactus, name="contact"),
    path('form', views.form, name='form'),
    path("newsdetails/<id>", views.news_details)
]



