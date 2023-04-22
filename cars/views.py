from django.shortcuts import render
from cars.models import Car

def cars_view(request):

    cars = Car.objects.all()
    getSearch = request.GET.get('search')

    if getSearch:
        cars = cars.filter(model__icontains=getSearch)

    return render(request,'cars.html',{"cars" : cars})
