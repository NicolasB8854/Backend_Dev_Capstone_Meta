from django.db import models


class Booking(models.Model):
    name = models.CharField(max_length=255)
    number_of_guests = models.IntegerField()
    booking_date = models.DateTimeField()

class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()
    menu_item_description = models.TextField(max_length=1000, default='') 
    def __str__(self):
        return f'{self.title} : {str(self.price)}'