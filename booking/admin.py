from django.contrib import admin
from .models import RunName, Customer, Booking


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('customer_id', 'full_name', 'email',)


@admin.register(RunName)
class RunNameAdmin(admin.ModelAdmin):
    list_display = ('runs',)


@amdin.register(booking)
class BookingAdmin(admin.ModelAdmin):
    search_fields = ['run_name']
    list_filter = ('run_name', 'status')
    list_display = ('booking_id', 'run_name', 'customer', 'status', 'requested_date',)
    
