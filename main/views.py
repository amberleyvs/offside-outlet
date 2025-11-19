import json
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core import serializers
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse
from django.utils import timezone
from django.utils.html import strip_tags
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_http_methods
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect
from django.views.generic import CreateView
from django.contrib.auth import login
from django.contrib.auth.models import User
from django import forms
import requests
from django.views.decorators.csrf import csrf_exempt
from django.utils.html import strip_tags
import json
from django.http import JsonResponse

from .models import Product, Car, Employee
from .forms import ProductForm, CarForm


# helper to check if ajax
def is_ajax(request):
    return request.headers.get("x-requested-with") == "XMLHttpRequest"


# MAIN VIEWS
@login_required(login_url='/login')
def show_main(request):
    """Main product listing page."""
    products = Product.objects.all().prefetch_related('wishlisted_by')
    
    wishlist_ids = []
    if request.user.is_authenticated:
        wishlist_ids = list(
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
        'user_logged': request.user.username,
        'wishlist_ids': wishlist_ids,
    }
    return render(request, "main.html", context)


@login_required(login_url="/login")
def wishlist_page(request):
    """Display user's wishlist."""
    products = Product.objects.filter(
        wishlisted_by=request.user
    ).prefetch_related("wishlisted_by")
    
    wishlist_ids = list(
        Product.objects.filter(wishlisted_by=request.user)
        .values_list('id', flat=True)
    )
    
    context = {
        "products": products,
        "last_login": request.COOKIES.get("last_login", "Never"),
        "wishlist_ids": wishlist_ids,
    }
    return render(request, "wishlist.html", context)


def show_detail(request, id):
    """Show individual product detail."""
    product = get_object_or_404(Product, pk=id)
    return render(request, 'show_detail.html', {'product': product})

# PRODUCT CRUD
@login_required(login_url='/login')
def add_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product = form.save(commit=False)
        product.user = request.user
        product.save()
        return redirect('main:show_main')

    return render(request, "add_product.html", {'form': form})


def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)
    form = ProductForm(request.POST or None, instance=product)
    
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')

    return render(request, "edit_product.html", {'form': form})


def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

# AJAX ENDPOINTS
@csrf_exempt
@require_POST
def add_product_entry_ajax(request):
    data = request.POST.copy()
    data['name'] = strip_tags(data.get('name', ''))

    form = ProductForm(data)
    if not form.is_valid():
        return JsonResponse({"errors": form.errors}, status=400)

    product = form.save(commit=False)
    if request.user.is_authenticated:
        product.user = request.user
    product.save()

    return HttpResponse(b"CREATED", status=201)


@require_POST
def update_product_entry_ajax(request, id):
    product = get_object_or_404(
        Product, pk=id,
        user=request.user if request.user.is_authenticated else None
    )
    form = ProductForm(request.POST, instance=product)
    
    if not form.is_valid():
        return JsonResponse({"errors": form.errors}, status=400)
    
    form.save()
    return JsonResponse({"status": "updated", "id": product.id})


@require_POST
def delete_product_ajax(request, id):
    product = get_object_or_404(
        Product, pk=id,
        user=request.user if request.user.is_authenticated else None
    )
    product.delete()
    return JsonResponse({"status": "deleted", "id": id})


@login_required(login_url="/login")
@require_POST
def toggle_wishlist(request, id):
    product = get_object_or_404(Product, pk=id)

    wished = product.wishlisted_by.filter(id=request.user.id).exists()
    if wished:
        product.wishlisted_by.remove(request.user)
        wished = False
    else:
        product.wishlisted_by.add(request.user)
        wished = True

    if is_ajax(request):
        return JsonResponse({"wishlisted": wished, "id": product.id})

    return redirect(request.POST.get("next") or "main:show_main")

def show_json(request):
    qs = Product.objects.all()

    if request.GET.get("wishlist") and request.user.is_authenticated:
        qs = qs.filter(wishlisted_by=request.user)

    data = [
        {
            "id": p.id,
            "name": p.name,
            "price": p.price,
            "discount": p.discount,
            "final_price": p.price_after_discount(),
            "description": p.description,
            "thumbnail": p.thumbnail,
            "category": p.category,
            "is_featured": p.is_featured,
            "is_limited": p.is_limited,
            "stock": p.stock,
            "user_id": p.user_id,
        }
        for p in qs
    ]
    return JsonResponse(data, safe=False)


def show_json_by_id(request, id):
    try:
        p = Product.objects.select_related('user').get(pk=id)
        return JsonResponse({
            "id": p.id,
            "name": p.name,
            "price": p.price,
            "discount": p.discount,
            "final_price": p.price_after_discount(),
            "description": p.description,
            "thumbnail": p.thumbnail,
            "category": p.category,
            "is_featured": p.is_featured,
            "is_limited": p.is_limited,
            "stock": p.stock,
            "user_id": p.user_id,
            "user_username": getattr(p.user, "username", None),
            "wishlisted_by": list(p.wishlisted_by.values_list('id', flat=True)),
        })
    except Product.DoesNotExist:
        return JsonResponse({'detail': 'Not found'}, status=404)


def show_xml(request):
    products = Product.objects.all()
    xml_data = serializers.serialize("xml", products)
    return HttpResponse(xml_data, content_type="application/xml")


def show_xml_by_id(request, id):
    try:
        product = Product.objects.filter(pk=id)
        xml_data = serializers.serialize("xml", product)
        return HttpResponse(xml_data, content_type="application/xml")
    except Product.DoesNotExist:
        return HttpResponse(status=404)

# AUTHENTICATION
@require_http_methods(["GET", "POST"])
def register(request):
    if request.method == "GET":
        return render(request, "register.html", {"form": UserCreationForm()})

    form = UserCreationForm(request.POST)

    if is_ajax(request):
        if form.is_valid():
            user = form.save()
            return JsonResponse({
                "ok": True,
                "message": "Account created",
                "redirect": reverse("main:login"),
            }, status=201)
        return JsonResponse({
            "ok": False,
            "message": "Register failed",
            "errors": form.errors,
            "non_field_errors": form.non_field_errors(),
        }, status=400)

    # Non-AJAX
    if form.is_valid():
        form.save()
        messages.success(request, "Registered! Please login")
        return redirect("main:login")

    messages.error(request, "Registration Failed.")
    return render(request, "register.html", {"form": form})

@require_http_methods(["GET", "POST"])
def login_user(request):
    if request.method == "GET":
        return render(request, "login.html", {"form": AuthenticationForm()})

    form = AuthenticationForm(request, data=request.POST)

    if is_ajax(request):
        if form.is_valid():
            login(request, form.get_user())
            return JsonResponse({
                "ok": True,
                "message": "Logged in",
                "redirect": reverse("main:show_main"),
            })
        return JsonResponse({
            "ok": False,
            "message": "Login failed",
            "errors": form.errors,
            "non_field_errors": form.non_field_errors(),
        }, status=400)

    # Non-AJAX
    if form.is_valid():
        login(request, form.get_user())
        messages.success(request, "Berhasil login.")
        resp = redirect("main:show_main")
        resp.set_cookie(
            "last_login",
            timezone.now().isoformat(),
            max_age=30 * 24 * 3600,
            samesite="Lax",
        )
        return resp

    messages.error(request, "Wrong email or password")
    return render(request, "login.html", {"form": form})

@require_http_methods(["POST"])
def logout_user(request):
    logout(request)

    if is_ajax(request):
        resp = JsonResponse({
            "ok": True,
            "message": "Logged out",
            "redirect": reverse("main:login"),
        })
    else:
        messages.success(request, "You are logged out")
        resp = redirect("main:login")

    resp.delete_cookie("last_login")
    return resp

def add_car(request):
    form = CarForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        car = form.save(commit=False)
        car.user = request.user
        car.save()
        return redirect('main:show_main')

    return render(request, "add_car.html", {'form': form})

def addEmployee(request):
    Employee.objects.create(name="Amberley", age=17, persona="cewe")
    return HttpResponse("Employee added successfully.")


def showEmployees(request):
    employees = Employee.objects.all()
    return render(request, "show.html", {"employees": employees})

def proxy_image(request):
    image_url = request.GET.get('url')
    if not image_url:
        return HttpResponse('No URL provided', status=400)
    
    try:
        response = requests.get(image_url, timeout=10)
        response.raise_for_status()
        
        return HttpResponse(
            response.content,
            content_type=response.headers.get('Content-Type', 'image/jpeg')
        )
    except requests.RequestException as e:
        return HttpResponse(f'Error fetching image: {str(e)}', status=500)
    
@csrf_exempt
def create_product_flutter(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = strip_tags(data.get("name", "")) 
        description = strip_tags(data.get("description", ""))  
        price = int(data.get("price", 0))
        category = data.get("category", "other")
        thumbnail = data.get("thumbnail", "")
        
        is_featured = data.get("is_featured", False)
        if isinstance(is_featured, str):
            is_featured = is_featured.lower() == 'true'
        
        stock = int(data.get("stock", 0))
        discount = int(data.get("discount", 0))
        
        is_limited = data.get("is_limited", False)
        if isinstance(is_limited, str):
            is_limited = is_limited.lower() == 'true'
        
        user = request.user
        
        new_product = Product(
            name=name, 
            description=description,
            price=price,
            category=category,
            thumbnail=thumbnail,
            is_featured=is_featured,
            stock=stock,
            discount=discount,
            is_limited=is_limited,
            user=user
        )
        new_product.save()
        
        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)