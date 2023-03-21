from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def products(request):
    return HttpResponse("Product page is Online...")

def about(request):
    return HttpResponse("About page is Online...")

def contact(request):
    return HttpResponse("Contact page is Online...")