from django.shortcuts import render

# Create your views here.
def desserts(request):
    return render(request, "desserts/desserts.html")
