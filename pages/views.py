from django.shortcuts import render
from .models import Chef
from desserts.models import Dessert, Locale

# Create your views here.
def home(request):
    chefs = Chef.objects.all()
    featured_desserts = Dessert.objects.filter(is_featured=True).order_by("dessert_name")
    fried_dough_desserts = Dessert.objects.filter(category="Fried Dough").order_by("dessert_name")
    category_search = Dessert.objects.values_list("category", flat=True).distinct()
    locale_name_search = Locale.objects.order_by("name").values_list("name", flat=True).distinct()


    data = {
        "chefs": chefs,
        "featured_desserts": featured_desserts,
        "fried_dough_desserts": fried_dough_desserts,
        #search fields
        "category_search": category_search,
        "locale_name_search": locale_name_search,
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
