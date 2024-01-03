from django.db import models

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# class User(AbstractUser):
#   pass

# models.py
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Car(models.Model):
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    color = models.CharField(max_length=20, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to='car_images/', null=True)

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"


class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.ForeignKey('Location', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Location(models.Model):
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.city}, {self.country}"

class Order(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()

    def __str__(self):
        return f"{self.quantity} {self.car} for {self.customer_name}"

# models.py
from django.db import models
from django.contrib.auth.models import User

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    items = models.ManyToManyField('Car', through='CartItem')

class CartItem(models.Model):
    car = models.ForeignKey('Car', on_delete=models.CASCADE)
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
