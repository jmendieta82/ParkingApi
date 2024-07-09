from django.contrib.auth.models import AbstractUser
from django.db import models


class Employee(AbstractUser):
    identification = models.CharField(max_length=11, default='', null=True, blank=True)
    phone = models.CharField(max_length=12, default='', null=True, blank=True)
    direction = models.CharField(max_length=255, default='', null=True, blank=True)


class Owner(models.Model):
    full_name = models.CharField(max_length=100, default='', null=True, blank=True)
    phone_number = models.CharField(max_length=20,unique=True)


class Brand(models.Model):
    name = models.CharField(max_length=100, default='', null=True, blank=True)
    active = models.BooleanField(default=True)


class Car(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.PROTECT)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT)
    license_plate = models.CharField(max_length=10)
    color = models.CharField(max_length=50, default='', null=True, blank=True)


class ParkingSpot(models.Model):
    size = models.CharField(max_length=50)  # Grande Mediano, Pequeño
    location = models.CharField(max_length=50)  #Sector del parqueadero
    is_occupied = models.BooleanField(default=False)


class Ticket(models.Model):
    entry_time = models.DateTimeField(auto_now_add=True)
    exit_time = models.DateTimeField(null=True)
    cost = models.DecimalField(max_digits=6, decimal_places=2,default=0)
    owner = models.ForeignKey(Owner, on_delete=models.PROTECT)
    car = models.ForeignKey(Car, on_delete=models.PROTECT)
    parking_spot = models.ForeignKey(ParkingSpot, on_delete=models.PROTECT)
