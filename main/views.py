from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core import serializers
from .models import Product
from .forms import AddForms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags
import json

@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get("filter", "all")  # default 'all'

    if filter_type == "all":
        products = Product.objects.all()
    else:
        products = Product.objects.filter(user=request.user)

    context = {
        'npm' : '2406436410',
        'name': request.user.username,
        'class': 'PBP A',
        'products_list': products,
        'last_login': request.COOKIES.get('last_login', 'Never')
    }
    return render(request, "main.html", context)

def show_xml(request):
    products = Product.objects.all()
    xml_data = serializers.serialize("xml", products)
    return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    products = Product.objects.all()
    data = [
        {
            "pk": product.id,
            "fields": {
                "name": product.name,
                "price": product.price,
                "thumbnail": product.thumbnail,
                "description": product.description,
                "category": product.category,
                "is_featured": product.is_featured,
                "user_id": product.user.id if product.user else None
            }
        }
        for product in products
    ]
    return JsonResponse(data, safe=False)

def show_xml_by_id(request, id):
    products = Product.objects.filter(pk=id)
    xml_data = serializers.serialize("xml", products)
    return HttpResponse(xml_data, content_type="application/xml")

def show_json_by_id(request, id):
    try:
        product = Product.objects.select_related('user').get(pk=id)
        data = {
            'id': product.id,
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'thumbnail': product.thumbnail,     # frontend akan memakai `thumbnail`
            'category': product.category,
            'is_featured': product.is_featured,
            'user_id': product.user.id if product.user else None,
            'user_username': product.user.username if product.user else 'Anonymous',
        }
        return JsonResponse(data)
    except Product.DoesNotExist:
        return JsonResponse({'detail': 'Not found'}, status=404)

@login_required(login_url='/login')
def add_product(request):
    if request.method == "POST":
        form = AddForms(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            return redirect('main:show_main')
    else:
        form = AddForms()
    return render(request, "add_product.html", {"form": form})

def product_detail(request, id):
    product = get_object_or_404(Product, pk=id)
    context = {
        "product": product,
        "product_id": product.id,  
    }
    return render(request, "product_detail.html", context)

@csrf_exempt
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'success', 'message': 'Your account has been successfully created!'})
        return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Invalid method'}, status=405)

@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = JsonResponse({'status': 'success', 'message': 'Login successful!'})
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Invalid method'}, status=405)

@login_required(login_url='/login')
def logout_user(request):
    logout(request)
    response = JsonResponse({'status': 'success', 'message': 'Logout successful!'})
    response.delete_cookie('last_login')
    return response

@csrf_exempt
@login_required(login_url='/login')
@csrf_exempt
@login_required(login_url='/login')
def edit_product(request, id):
    product = get_object_or_404(Product, pk=id, user=request.user)

    if request.method == "POST":
        form = AddForms(request.POST, instance=product)
        if form.is_valid():
            updated_product = form.save(commit=False)
            updated_product.user = request.user
            updated_product.save()
            return JsonResponse({'status': 'success', 'message': 'Product updated!'})
        return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)

    # kalau GET 
    else:
        data = {
            'name': product.name,
            'description': product.description,
            'price': product.price,              # ⬅️ tambahkan ini
            'category': product.category,
            'thumbnail': product.thumbnail,
            'is_featured': product.is_featured,
        }
        return JsonResponse(data)

@login_required(login_url='/login')
def delete_product(request, id):
    product = get_object_or_404(Product, pk=id, user=request.user)  
    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

@csrf_exempt
@login_required(login_url='/login')
def add_product_ajax(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description', '')
        price = int(request.POST.get('price', 0))
        category = request.POST.get('category', '')
        thumbnail = request.POST.get('thumbnail', '')
        is_featured = request.POST.get('is_featured') == 'on'

        new_product = Product.objects.create(
            user=request.user,
            name=name,
            description=description,
            price=price,
            category=category,
            thumbnail=thumbnail,
            is_featured=is_featured,
        )

        return JsonResponse({
            'id': new_product.id,
            'name': new_product.name,
        }, status=201)
    return JsonResponse({'error': 'Invalid method'}, status=405)
