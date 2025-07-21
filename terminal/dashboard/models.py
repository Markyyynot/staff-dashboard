from django.db import models

# Create your models here.

class Ticket(models.Model):
    passenger_name = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    destination = models.CharField(max_length=100)
    departure_time = models.DateTimeField()
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.passenger_name} - {self.destination}"