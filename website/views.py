from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def sign_up(request):
    if request.method == "POST":
        form = Customer(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'signup.html', {'form': form})
    else:
        form = Customer()
        return render(request, 'signup.html', {'form': form})


def get_customer_instance(request):
    customer_email = request.user.email
    customer = Customer.objects.filter(email=customer_email).first()

    return customer
    

