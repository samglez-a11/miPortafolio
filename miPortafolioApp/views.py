from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request, "miPortafolioApp/home.html")

def trabajos(request):
    return render(request, "miPortafolioApp/trabajos.html")

def about(request):
    return render(request, "miPortafolioApp/about.html")

def hobby(request):
    return render(request, "miPortafolioApp/hobby.html")