from django.shortcuts import render
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User, auth
from django.urls import reverse
from django.http import HttpResponseRedirect, JsonResponse
from .models import Doctors
import pandas as pd
from scipy.sparse import hstack
import joblib
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
    return render(request, 'templates/landingPage.html')



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


encoder, tfidf_vectorizer, rf_icd10, rf_treatment = joblib.load("/Users/siddharth/Desktop/Hackathon DI/suggestAI/mentalIllness/medical_predictor_model2.pkl")

def predict_input( input_tuple):
    input_data = pd.DataFrame([input_tuple], columns=['Problem Summary', 'Problem Category', 'Psychological Category'])

    # Transform input data
    input_encoded = encoder.transform(input_data[['Problem Category', 'Psychological Category']])
    input_summary = tfidf_vectorizer.transform(input_data['Problem Summary'])
    input_combined = hstack((input_encoded, input_summary))

    # Make predictions
    icd10_prediction = rf_icd10.predict(input_combined)[0]
    treatment_prediction = rf_treatment.predict(input_combined)[0]

    return icd10_prediction, treatment_prediction

test = joblib.load('/Users/siddharth/Desktop/Hackathon DI/suggestAI/mentalIllness/m2.pkl')

def predict(request):
    if request.method == 'POST':
        data = request.POST
        age = data['age']
        gender = data['gender']
        problem_description = data['problem_description']
        op1=test.predict({"age":age,"gender":gender,"problem_description":problem_description})
        op3=op1
        op1=tuple(op1[0][0:3])
        icd10_pred, treatment_pred = predict_input(op1)
        print(icd10_pred)
        print(treatment_pred)
        return HttpResponse(icd10_pred+','+icd10_pred+str(op3))
    return render(request, 'templates/inputPage.html')
    
        
    
    
