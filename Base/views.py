from django.shortcuts import render,HttpResponse, redirect
from datetime import datetime
from Base.models import login
from Base.models import reservation

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')
    
def menu(request):
    return render(request, 'menu.html')
    

def reservation(request):
    if request.method == 'POST':
        name= request.POST.get('name')
        number= request.POST.get('number')  
        email= request.POST.get('email')
        person= request.POST.get('person')  
        date= request.POST.get('date')

        obj = reservation()
        obj.Name = name
        obj.Phone_number = number
        obj.Email = email
        obj.Total_person = person
        obj.Booking_date = date
        obj.save()
        return redirect(request, 'reservation.html')
    else:
        return render(request, 'reservation.html')



    
       
    

    # Pass the API key to the template


    
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        obj = login()
        obj.Username = username
        obj.Password = password
        obj.save()
        return redirect('/home')
    else:
        return render(request, 'login.html')
        


 


