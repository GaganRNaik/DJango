from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect

# Create your views here.
def say_hello(request):
    return render(request,'sample.html',{"name":"gagan"})

def xyz(request):
    return render(request,'clock.html')

def register_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')

        # Create a new user
        user = User.objects.create(username=username, email=email, password=make_password(password))
        return HttpResponse("User registered successfully!")
    return render(request, 'register.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('products')  # Redirect to a success page or dashboard
        else:
            return HttpResponse("Invalid credentials!")
    return render(request, 'login.html')

def products(request):
    product_list = [
        {"name": "Product 1", "price": "$10"},
        {"name": "Product 2", "price": "$20"},
        {"name": "Product 3", "price": "$30"},
    ]
    return render(request, 'products.html', {"products": product_list})