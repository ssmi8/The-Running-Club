from django.contrib import admin
from .models import Booking, Home, Booking_detail
from django_summernote.admin import SummernoteModelAdmin


admin.site.register(Booking)

admin.site.register(Home)

admin.site.register(Booking_detail)
