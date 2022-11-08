from django.shortcuts import render
from django.http import HttpResponse
from .models import AutoModels, Car, Order, OderLine, Services


def index(request):
    # Suskaičiuokime keletą pagrindinių objektų
    num_cars = Car.objects.all().count()
    num_orders = Order.objects.all().count()

    # Laisvos knygos (tos, kurios turi statusą 'g')
    num_orders_available = OderLine.objects.filter(status__exact='a').count()

    # perduodame informaciją į šabloną žodyno pavidale:
    context = {
        'num_cars': num_cars,
        'num_orders': num_orders,
        'num_orders_available': num_orders_available,
    }

    # renderiname index.html, su duomenimis kintamąjame context
    return render(request, 'index.html', context=context)
