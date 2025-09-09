from django.shortcuts import render
from .models import Product

def show_main(request):
    products = Product.objects.all()

    context = {
        'npm' : '2406436410',
        'name': 'Aghnaya Kenarantanov',
        'class': 'PBP A',
        'products': products,
    }

    return render(request, "main.html", context)