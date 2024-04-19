from django.shortcuts import render
from .models import Chef

# Create your views here.
def home(request):
    chefs = Chef.objects.all()
    data = {
        "chefs": chefs,
    }
    return render(request, "pages/home.html", data)


def about(request):
    chefs = Chef.objects.all()
    data = {
        "chefs": chefs,

    }
    return render(request, "pages/about.html", data)

def ingredients(request):
    return render(request, "pages/ingredients.html")

def contact(request):
    return render(request, "pages/contact.html")

def locale(request):
    return render(request, "pages/locale.html")
