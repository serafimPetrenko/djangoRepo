from django.shortcuts import render
from .models import Pharmacy, Pills, Info


def index(request):
    return render(request, 'main/index.html')


def pharmacy_page(request):
    pharmacy_items = Pharmacy.objects.order_by('number')
    return render(request, 'main/pharmacy.html', {'pharmacy_items': pharmacy_items})


def pills_page(request):
    pills_items = Pills.objects.order_by('name')
    return render(request, 'main/pills.html', {'pills_items': pills_items})


def info_page(request):
    info_items = Info.objects.order_by('-id')
    return render(request, 'main/info.html', {'info_items': info_items})

# Create your views here.
