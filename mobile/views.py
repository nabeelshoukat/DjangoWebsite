from django.shortcuts import render
from django.http import HttpResponse
from .models import MobileModel,News
# Create your views here.
def indexmob(request):
    mob_data=MobileModel.objects.all().order_by('-brand')
    news_data=News.objects.all()
    for i in news_data:
        print(i.news_title)
    data ={
        "mob_data":mob_data,
        "news_data":news_data

    }

    return render(request,"boot.html",data)
def news_details(requst,id):
    print(id)
    return render(requst,"newsdetails.html")