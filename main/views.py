from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.core import serializers
from .models import Employee
from .models import Product
from .forms import ProductForm

# Create your views here.
def show_main(request):

    products = Product.objects.all()

    context = {
        "app_name": "Offside Outlet",
        "student_name": "Amberley Vidya",
        'NPM': "2406495533",
        'class': 'PBP E',
        'products': products
    }

    return render(request, "main.html", context)

def addEmployee(request):
    Employee.objects.create(name="Amberley", age=17, persona="cewe")
    return HttpResponse("Employee added successfully.")

def showEmployees(request):
    employees = Employee.objects.all()
    context = {
        "employees": employees
    }
    return render(request, "show.html", context)

def add_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "add_product.html", context)

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

def show_xml_by_id(request, product_id):
    try:
        product = Product.objects.filter(pk=product_id)
        xml_data = serializers.serialize("xml", product)
        return HttpResponse(xml_data, content_type="application/xml")
    except Product.DoesNotExist:
        return HttpResponse(status=404)

def show_json_by_id(request, product_id):  
    try:
        product = Product.objects.get(pk=product_id)
        json_data = serializers.serialize("json", [product])
        return HttpResponse(json_data, content_type="application/json")
    except Product.DoesNotExist:
        return HttpResponse(status=404)