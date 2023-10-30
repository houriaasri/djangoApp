from django.db import models

class Booking(models.Model):
    first_name = models.CharField(max_length=100)
    reservation_date = models.DateField()
    reservation_slot = models.CharField(max_length=50)
