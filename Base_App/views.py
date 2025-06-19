from django.shortcuts import render

# Create your views here.
def HomeView(request):
    return render(request, 'home.html')

def AboutView(request):
    return render(request, 'about.html')

def MenuView(request):
    return render(request, 'menu.html')

def BookTableView(request):
    return render(request, 'book.html')

def ContactView(request):
    return render(request, 'contact.html')