from django.db import models


class Booking(models.Model):
    Name = models.CharField(max_length=255)
    NO_OF_GUESTS = models.IntegerField()
    BookingDate = models.DateTimeField()

class Menu(models.Model):
    Title = models.CharField(max_length=255)
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    Inventory = models.IntegerField()