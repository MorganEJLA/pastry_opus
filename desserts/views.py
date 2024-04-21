from django.shortcuts import render, get_object_or_404
from .models import Dessert
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
def desserts(request):
    all_desserts = Dessert.objects.all()
    paginator = Paginator(all_desserts, 8)
    page = request.GET.get("page")
    paged_desserts = paginator.get_page(page)
    data = {
        "desserts": paged_desserts,
    }
    return render(request, "desserts/desserts.html", data)

def dessert_detail(request, id):
    single_dessert = get_object_or_404(Dessert, id=id)
    first_ingredient = single_dessert.featured_ingredient.first()

    if first_ingredient and first_ingredient.photo:
        banner_image = first_ingredient.photo.url
    else:
        banner_image = "media/photos/default.jpg"
    data = {
        "single_dessert": single_dessert,
        "page_title": single_dessert.dessert_name,
        "background_image": banner_image,
    }
    return render(request, "pages/dessert_detail.html", data)

def search(request):
    desserts = Dessert.objects.all()
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            desserts = desserts.filter(description__icontains=keyword)
    data = {
        "desserts": desserts,
    }
    return render(request, "desserts/search.html", data)
