from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django import forms


# Create model for booking a running session


class Booking(models.Model):
    BEGINNERS = 'B'
    INTERMEDIATE = 'I'
    ADVANCED = 'A'
    SESSIONS_CHOICES_CHOICES = [
        (BEGINNERS, 'Running group for beginners level'),
        (INTERMEDIATE, 'Running group for intermediate level'),
        (ADVANCED, 'Running group for advanced runners'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    booking_date_time = models.DateTimeField(auto_now=False, blank=True)

    confirmed = models.BooleanField(default=False)


class Home(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
