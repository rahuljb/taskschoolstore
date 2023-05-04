from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def home(request):
    return render(request, "index.html")


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('button')
        else:
            messages.info(request, "Invalid User Name")
            return redirect("login")
    return render(request, "login.html")


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        conpassword = request.POST['conpassword']
        if password == conpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "User id Already Taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password)
            user.save()
            print("User created")
            return redirect("login")
        else:
            messages.info(request, "Password Not Matched")
            print("Password error")
            return redirect('register')
    return render(request, "register.html")


def logout(request):
    auth.logout(request)
    return redirect('/')


def form(request):
    return render(request, "form.html")


def button(request):
    return render(request, "button.html")


def success(request):
        messages.info(request, 'Order Placed Successfully')
        return render(request, "success.html")
