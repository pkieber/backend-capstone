from django.db import models
from django.core.validators import MaxValueValidator
from django.utils import timezone


class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField(default=6, validators=[MaxValueValidator(200)])
    booking_date = models.DateField(default=timezone.now)
    # booking_slot = models.SmallIntegerField(default=10)
    
    def __str__(self):
        return f'{self.name}: {self.booking_date}'


class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField(default=5)

    def __str__(self):
        return f'{self.title} : {str(self.price)}'