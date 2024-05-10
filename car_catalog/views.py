from django.shortcuts import render, redirect
from car_catalog.models import Car, CarCatalog
from django.contrib import messages
from django.db import transaction


def index(request):
    catalog = CarCatalog.objects.first()
    if not catalog:
        catalog = CarCatalog.objects.create()
    cars = Car.objects.all()
    context = {
        'catalog': catalog,
        'cars': cars,
        'admin_logged_in': request.session.get('admin_logged_in', False)
    }
    return render(request, 'car_catalog/index.html', context)


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == 'admin' and password == 'Passw0rd1':
            request.session['admin_logged_in'] = True
            messages.success(request, 'Login successful!')
            return redirect('index')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'car_catalog/login.html')

from django.shortcuts import render, redirect
from .models import Car
from django.contrib import messages

def add_car(request):
    if request.method == 'POST':
        make = request.POST['make']
        model = request.POST['model']
        year = request.POST['year']
        price = request.POST['price']
        new = 'new' in request.POST
        image = request.FILES.get('image')

        car = Car(make=make, model=model, year=year, price=price, new=new, image=image)
        car.save()
        messages.success(request, 'Car added successfully.')
        return redirect('index')

    return render(request, 'car_catalog/add_car.html')


def about(request):
    # Fetch any data needed for the about page
    context = {
        'dealer_address': '123 Main Street, Anytown USA',
        'dealer_phone': '555-555-5555',
        'dealer_hours': 'Monday - Saturday, 9am - 6pm'
    }
    return render(request, 'car_catalog/about.html', context)

from django.db import transaction
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Car

@transaction.atomic
def delete_car(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    if request.method == 'POST':
        car.delete()
        messages.success(request, 'Car deleted successfully.')
        return redirect('index')
    return render(request, 'car_catalog/delete_car.html', {'car': car})
