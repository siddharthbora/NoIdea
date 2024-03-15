from django.shortcuts import render
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User, auth
from django.urls import reverse
from django.http import HttpResponseRedirect, JsonResponse
from .models import Doctors
def index(request ):
    return HttpResponse("hello")
def reg(request):
    if request.method == 'POST':
        data = request.POST
        username = data['username']
        firstname = data['firstname']
        lastname = data['lastname']
        email = data['email']
        phone = data['phone']
        # specialization = data['specialization']
        password = data['password']
        conf_pass = data['confirm_password']
        if not str(firstname).isalpha():
            return render(request, 'templates/reg.html', {'msg': ["First Name is not Valid"]})
        if not str(lastname).isalpha():
            return render(request, 'templates/reggreg.html', {'msg': ["Last Name is not Valid"]})
        if not str(phone).isnumeric() and len(phone) == 10 and phone < 59999999999:
            return render(request, 'templates/reg.html', {'msg': ["Invalid Phone Number is Entered"]})
        if password != conf_pass:
            return render(request, 'templates/reg.html', {'msg': ["Passwords Don't match"]})
        if len(password) == 0:
            return render(request, 'templates/reg.html', {'msg': ["Please enter password"]})
        try:
            ouruser = User.objects.create_user(username=username, first_name=firstname, email=email, password=password,
                                               last_name=lastname)
            newuser = Doctors(user=ouruser, phone=phone,
                               specialization='specialization')
            ouruser.save()
            newuser.save()
            return HttpResponse("hello")
        except Exception as e:
            return render(request, 'templates/reg.html', {'msg': ['User already exists..!!']})
    return render(request, 'templates/reg.html', {'msg': ""})


def home(request):
    return render(request, 'templates/home.html')



def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Retrieving user using Django's built-in User model
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return HttpResponse(f"Hello ")  # Successful login
        else:
            return HttpResponse("ERROR")  # Incorrect credentials

    return render(request, 'templates/login.html')  # Rendering the login template

