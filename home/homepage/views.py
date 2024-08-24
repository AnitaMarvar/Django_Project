from django.shortcuts import render,HttpResponse
from homepage.models import Contact
from django.contrib import messages
from datetime import datetime
# Create your views here.
def index(request):
    return render(request,"index.html")
def basics(request):
    return render(request,"basics.html")
def emergency_numbers(request):
    return render(request,"emergency_numbers.html")
def cpr(request):
    return render(request,"cpr.html")
def burns(request):
    return render(request,"burns.html")
def tips_tutorials(request):
    return render(request,"tips_tutorials.html")
def about(request):
    return render(request,"about.html")
def cuts(request):
    return render(request,"cuts.html")
def choking(request):
    return render(request,"choking.html")
def contacts(request):
    if request.method=="POST":
        email=request.POST.get('email')
        password=request.POST.get('password')
        city=request.POST.get('city')
        state=request.POST.get('state')
        name=request.POST.get('first name')
        contact = Contact(email=email,password=password,city=city,state=state,name=name, date=datetime.now())
        contact.save()
        messages.success(request,"Form has been successfully sent.")
    return render(request,"contacts.html")