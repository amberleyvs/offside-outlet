from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        "app_name": "Offside Outlet",
        "student_name": "Amberley Vidya",
        'NPM': "2406495533",
        'class': 'PBP E'
    }

    return render(request, "main.html", context)