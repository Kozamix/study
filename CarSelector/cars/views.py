from django.shortcuts import render, redirect, get_object_or_404
from .models import Car
from .forms import CarForm

def edit_car(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES, instance=car)
        if form.is_valid():
            form.save()
            return redirect('car_list')
    else:
        form = CarForm(instance=car)
    return render(request, 'cars/edit_car.html', {'form': form, 'car': car})

def add_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('car_list')
        else:
            # If the form is not valid, you might want to handle this case
            # For example, you can re-render the form with validation errors
            return render(request, 'cars/add_car.html', {'form': form})
    else:
        form = CarForm()

    return render(request, 'cars/add_car.html', {'form': form})

def car_list(request):
    cars = Car.objects.all()
    return render(request, 'cars/home.html', {'cars': cars})

    return render(request, 'base.html')


def car_detail_view(request, pk):
    car = get_object_or_404(Car, pk=pk)
    return render(request, 'cars/car_detail.html', {'car': car})