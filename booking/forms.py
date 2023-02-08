from .models import Booking
from django import forms
from django.forms import ModelForm
from django.contrib.admin import widgets


class BookingForm(ModelForm):
    booking_date_time = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
    )

    class Meta:
        model = Booking
        exclude = ["confirmed", "user"]
