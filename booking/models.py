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
    RUN_STATUS = (('Fully_Booked', 'Fully_Booked'), ('Available', 'Available'))
    
    CHOICE_STATUS = (('Yes', 'y'), ('No', 'n'), ('Pending', 'p'))
    
    class Meta:
        verbose_name_plural = 'Bookings'
        
        booking_id = models.AutoField(primary_key=True)
        customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="customer", null=True)
        run_name = models.ForeignKey('Run_Name', on_delete=models.CASCADE, default=True)
        status = models.CharField(max_length=20, choices=CHOICE_STATUS, default='Available')
        spots = models.IntegerField(default=True, null=False, validators=[
            MaxValueValidator(30), MinValueValidator(1)])
        requested_date = models.DateField()
        bookingstatus = models.CharField(max_length=20, default='p', choices=CHOICE_STATUS)

    def __str__(self):
        return str(self.run_name)

