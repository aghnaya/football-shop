from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core import serializers
from .models import Product
from .forms import AddForms

def show_main(request):
    products = Product.objects.all()

    context = {
        'npm' : '2406436410',
        'name': 'Aghnaya Kenarantanov',
        'class': 'PBP A',
        'products': products,
    }
    return render(request, "main.html", context)

def show_xml(request):
    products = Product.objects.all()
    xml_data = serializers.serialize("xml", products)
    return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    products = Product.objects.all()
    json_data = serializers.serialize("json", products)
    return HttpResponse(json_data, content_type="application/json")

def show_xml_by_id(request, id):
    products = Product.objects.filter(pk=id)
    xml_data = serializers.serialize("xml", products)
    return HttpResponse(xml_data, content_type="application/xml")

def show_json_by_id(request, id):
    products = Product.objects.filter(pk=id)
    json_data = serializers.serialize("json", products)
    return HttpResponse(json_data, content_type="application/json")

def add_product(request):
    if request.method == "POST":
        form = AddForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:show_main')
    else:
        form = AddForms()
    return render(request, "add_product.html", {"form": form})

def product_detail(request, id):
    product = get_object_or_404(Product, pk=id)
    return render(request, "product_detail.html", {"product" : product})