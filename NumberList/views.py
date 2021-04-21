from django.shortcuts import render
from .models import Numbers, Words

# Create your views here.
def index(request):
    numbers = Numbers.objects.all()
    words = Words.objects.all()
    return render(request, 'NumberList/index.html', {"Numbers" : numbers, "Words" : Words})
    