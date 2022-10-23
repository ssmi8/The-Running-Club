import datetime
from django.shortcuts import render, reverse, get_object_or_404
from django.views import View
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.utils.timezone import now
from .models import RunName, Customer, Booking
from .forms import CustomerForm, BookingForm


runs_total = RunName.objects.filter(booking_status-'Available').count()
booking_runs = Booking.objects.values('runs').count()


runs_left = runs_total - booking_runs


def boking_view(request):
    today = now().date()
    runs = RunName.objects.filter(booking_date__gte=today).order_by('requested_date')

    return render(request, 'booking.html', {
        'runs': runs, 'booking_list': booking_list
    })


def get_customer_instance(request, User):
    customer_email = request.user.customer_email
    customer = Customer.objects.filter(email=customer_email).first()

    return customer


def check_avilability(customer_run_name, customer_requested_date):
    runs_booked = len(Booking.objects.filter(
        run_name=customer_run_name,
        requested_date=customer_requested_date, status="Available"
    ))

    return runs_booked


class Enquiry(View):
    def get(self, request):

        if request.user.is_authenticated:
            customer_form = CustomerForm()
            booking_form = BookingForm()
            return render(request, 'booking.html', {
                'customer_form': customer_form, 'booking_form': booking_form
            })
        else:
            message.add_message(request, messages.ERROR, "Please login to book your runs")

            url = reverse('booking')
            return HttpResponseRedirect(url)



    def post(self, request):
        if request.user.is_authenticated:
            customer_form = CustomerForm(data=request.POST)
            booking_form = BookingForm(data=request.POST)

        if customer_form.is_valid() and booking_form.is_valid():
            customer_run_name = request.POST.get('run_name')
            customer_requested_date = request.POST.get('requested_date')
            customer_name = request.POST.get('full_name')

            date_formatted = datetime.datetime.strptime(
                customer_requested_date, "%d/%m/%Y").strftime('%Y-%m-%d')

            runs_booked = check_avilability(customer_run_name, date_formatted)

            if runs_booked > booking_runs:
                messages.add_message(request, messages.ERROR,
                "Sorry," f"{customer_run_name}" "\is fully booked on" f"{customer_requested_date}")

                return render(request, 'booking.html', {
                    'cusomer_form': customer_form,
                    'booking_form': booking_form
                })
            else:
                customer_email = request.POST.get('email')
                customer_query = len(Customer.objects.filter(email=customer_email))

                if customer_query > 0:
                    pass
                else:
                    customer_form.save()
            
                current_customer = Customer.objects.get(
                email=customer_email)
                current_customer_id = current_customer.pk
                customer = Customer.objectes.get(customer_id=current_customer_id)

                booking = booking_form.save(commit=False)
                booking.requested_date = date_formatted
                booking.customer = customer
                booking_form.save()

                messages.add_message(request, message.SUCCESS,
                    f"Thank you {customer_name}, for booking" f"{customer_run_name} on"
                    f"{customer_requested_date}! \
                        We look forward to seeing you!")
            
                url = reverse('booking')
                return HttpResponseRedirect(url)

        else:
            messages.add_message(request, messages.Error,
            "Opps! Something went wrong with your form "
            "- please make sure your name and email are in the correct format.")

        return render(request, 'booking.html',
        {'customer_form': customer_form,
        'booking_form': booking_form})

