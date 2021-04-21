from django.shortcuts import render 
from .models import Country, States, City

def index(request):
    c = Country.objects.all()
    s = States.objects.all()
    city = City.objects.all()
    return render(request, 'Lockdown/index.html', {"Country": c, "States": s, "City": city})