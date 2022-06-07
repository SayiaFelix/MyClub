from calendar import c
from pydoc import describe
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Venue(models.Model):
    name = models.CharField("Venue Name",max_length=120)
    address = models.CharField("Address",max_length=300)
    zip_code = models.CharField("Zip Code",max_length=15,blank=True)
    phone = models.CharField("Contact Number",max_length=30,blank=True)
    web = models.URLField('Website Address',blank=True)
    email_address = models.EmailField("Email Address",blank=True)


    def __str__(self):
        return self.name

class MyClubUser(models.Model):
    first_name = models.CharField('First Name',max_length=30)
    last_name = models.CharField('Last Name', max_length=30)
    email = models.EmailField('User Address')

    def __str__(self):
        return self.first_name + ' ' + self.last_name



class Event(models.Model):
    name = models.CharField('Events Name',max_length = 120)
    event_date = models.DateTimeField('Events Date') 
    venue = models.ForeignKey(Venue,on_delete=models.CASCADE,blank=True,null=True)
    manager = models.ForeignKey(User,on_delete=models.SET_NULL,blank=True,null=True)
    description= models.TextField(blank=True)
    attendees=models.ManyToManyField(MyClubUser,blank=True)

    def __str__(self):
        return self.name
    
class MoringaMerch(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=20)