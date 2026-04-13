from django.conf import settings
from django.db import models
from .register_apartments import RegisterApartments


class Booking(models.Model):

    apartment = models.ForeignKey(RegisterApartments, on_delete=models.CASCADE, related_name='bookings')
    status = models.CharField(max_length=10, choices=[('pending','Pending'),('confirmed','Confirmed'),('cancelled','Cancelled')], default='pending')

    # link on custom user
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='bookings')


    def __str__(self):
        return f"{self.apartment.title} booked by {self.user.username}"

    class Meta:
        db_table = 'booking'