from django.urls import path
from booking import views


urlpatterns = [
    path('', views.Enquiry.as_view(), name='booking'),
    path('manage_booking', views.ManageBooking.as_view(), name='manage_booking'),
    path('edit_booking/<booking_id>', views.EditBooking.as_view(), 
        name='edit_booking'),
    path('delete_booking/<booking_id>', views.DeletBooking.as_view(), 
        name='delete_booking'),
]