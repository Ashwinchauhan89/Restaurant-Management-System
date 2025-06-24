from django.db import models
# Create your models here.





class login(models.Model):
    Username = models.CharField(max_length=15)
    Password = models.CharField(max_length=15)

    


   
class reservation(models.Model):
    Name= models.CharField(max_length=100)
    Phone_number = models.CharField(max_length=15)
    Email = models.EmailField()
    Total_person = models.IntegerField(default=1)
    Booking_date = models.DateField(null=True, blank=True)
    

    

   



