from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.core import serializers
from .models import Product
from .forms import ProductForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseRedirect
import datetime
from .forms import CarForm
from .models import Car
from .models import Employee

# Create your views here.
@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get("filter", "all")  # default 'all'
    if filter_type == "all":
        products = Product.objects.all()
    else:
        products = Product.objects.filter(user=request.user)

    products = Product.objects.all().prefetch_related('wishlisted_by')

    wishlist_ids = set()
    if request.user.is_authenticated:
        wishlist_ids = set(
            Product.objects.filter(wishlisted_by=request.user)
                           .values_list('id', flat=True)
        )

    context = {
        "app_name": "Offside Outlet",
        "student_name": "Amberley Vidya",
        'NPM': "2406495533",
        'class': 'PBP E',
        'products': products,
        'last_login': request.COOKIES.get('last_login', 'Never'),
        'user_logged' : request.user.username,
        'wishlist_ids': wishlist_ids, 
    }

    return render(request, "main.html", context)

@login_required(login_url="/login")
def toggle_wishlist(request, id):
    # POST only to avoid CSRF via links
    if request.method != "POST":
        return redirect(request.POST.get("next") or "main:show_main")

    product = get_object_or_404(Product, pk=id)

    if product.wishlisted_by.filter(id=request.user.id).exists():
        product.wishlisted_by.remove(request.user)
    else:
        product.wishlisted_by.add(request.user)

    # go back where the user came from
    return redirect(request.POST.get("next") or "main:show_main")

@login_required(login_url="/login")
def wishlist_page(request):
    # show only this user’s wishlist
    products = Product.objects.filter(wishlisted_by=request.user).prefetch_related("wishlisted_by")
    context = {
        "products": products,
        "last_login": request.COOKIES.get("last_login", "Never"),
    }
    return render(request, "wishlist.html", context)

def addEmployee(request):
    Employee.objects.create(name="Amberley", age=17, persona="cewe")
    return HttpResponse("Employee added successfully.")

def showEmployees(request):
    employees = Employee.objects.all()
    context = {
        "employees": employees
    }
    return render(request, "show.html", context)

@login_required(login_url='/login')
def add_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product = form.save(commit=False)
        product.user = request.user
        product.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "add_product.html", context)

def add_car(request):
    form = CarForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product = form.save(commit=False)
        product.user = request.user
        product.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "add_car.html", context)

def show_detail(request, id):
    product = get_object_or_404(Product, pk=id)
    context = {
        'product': product
    }
    return render(request, 'show_detail.html', context)

def show_xml(request):
    products = Product.objects.all()
    xml_data = serializers.serialize("xml", products)
    return HttpResponse(xml_data, content_type="application/xml")


def show_json(request):
    products = Product.objects.all()
    json_data = serializers.serialize("json", products)
    return HttpResponse(json_data, content_type="application/json")

def show_xml_by_id(request, id):
    try:
        product = Product.objects.filter(pk=id)
        xml_data = serializers.serialize("xml", product)
        return HttpResponse(xml_data, content_type="application/xml")
    except Product.DoesNotExist:
        return HttpResponse(status=404)

def show_json_by_id(request, id):  
    try:
        product = Product.objects.get(pk=id)
        json_data = serializers.serialize("json", [product])
        return HttpResponse(json_data, content_type="application/json")
    except Product.DoesNotExist:
        return HttpResponse(status=404)
    
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
   else:
        form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')

    context = {
        'form': form
    }

    return render(request, "edit_product.html", context)

def delete_product(request, id):
    news = get_object_or_404(Product, pk=id)
    news.delete()
    return HttpResponseRedirect(reverse('main:show_main'))