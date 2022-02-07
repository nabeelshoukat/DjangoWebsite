from django.http import HttpResponseRedirect
from django.shortcuts import render
# from website.mobile.views import *
def index(request):
    return render(request, "index.html")


def about(request):

    return render(request, "about.html")


def contactus(request):
    return render(request, "contact.html")


def form(request):
    # sericeData = Service.objects.all() 
    # for i in sericeData:
    #     print("data",i)
    # print(Service)

    # lst=[]
    # if request.method=='POST':
    #     print('method is post')
    #     var = request.POST.get("mobile")
    #     lst.append(var)
    #     return HttpResponseRedirect("/")

    # print([i for i in lst])
    # servicedata =models.Service.objects.all()
    # print(servicedata)
    return render(request, "user_form.html", )


def news_details(requst, id):

    return render(requst, "newsdetails.html")
