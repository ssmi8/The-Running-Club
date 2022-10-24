from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=250, default="")

    def __str__(self):
        return self.full_name


class RunName(models.Model):

    NAME_OF_RUNS = (('Early_Grind', 'Early_Grind'),
                    ('Recovery_Run', 'Recovery_Run'), 
                    ('Twilight_Hustle', 'Twilight_Hustle'))
    
    runs = models.CharField(max_length=20, choices=NAME_OF_RUNS, primary_key=True)

    def __str__(self):
        return str(self.runs)


class Booking(models.Model):
      
    STATUS_CHOICES = (('Fully_Booked', 'Fully_Booked'),
                      ('Availble', 'Availble'))

    OPTION_STATUS = (('y', 'Yes'), ('n', 'No'), ('p', 'Pending'))

    class Meta:
        """Booking Meta"""
        verbose_name_plural = 'Bookings'

    booking_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name="customer", null=True)
    run_name = models.ForeignKey(
        'RunName', on_delete=models.CASCADE, default=True)
    status = models.CharField(
        max_length=15, choices=STATUS_CHOICES, default='Available')
    seats = models.IntegerField(default=True, null=False, validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ])
    requested_date = models.DateField()
    bookingtatus = models.CharField(
        max_length=10, default='p', choices=OPTION_STATUS)

    def __str__(self):
        return str(self.run_name)