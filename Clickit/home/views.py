from datetime import datetime
import email
from django.shortcuts import render, HttpResponse
from matplotlib.style import context
from home.models import Contact


def co (data):
    result = int(round((9 * float(data)) / 5 + 32))


# Create your views here.
def index (request):
    # # how to send a variable 
    # context = {
    #     "variable-name"  :" variable value", 
    # }
    # return render(request, "index.html", context)
    # return HttpResponse("this is index as home page")
    return render(request, "index.html")

def about (request):
    return render(request, "about.html")
    # return HttpResponse("this is about page")

def contact (request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name = name, email = email, phone = phone, desc = desc, date = datetime.today())
        contact.save()


    return render(request, "contact.html")
    # return HttpResponse("this is contact page")

def pricing (request):
    return render(request, "pricing.html")
    # return HttpResponse("this is pricing page")

def tools (request):
    return render(request, "tools.html")

def tools1 (request):
    data = request.POST.get("name")

    context = {
        "out"  : co(data), 
    }   
    return render(request, "tools1.html", context)
    # return HttpResponse("this is tools page")