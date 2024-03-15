from django.shortcuts import render
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User, auth
from django.urls import reverse
from django.http import HttpResponseRedirect, JsonResponse
from .models import Doctors
import pandas as pd
from scipy.sparse import hstack
import joblib
import requests

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

def listing(request):
    return render(request, 'templates/ListingPage.html')

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
def make_predictions_on_incoming_dataset(incoming_dataset, pipeline):
    incoming_data = pd.DataFrame([incoming_dataset])
    incoming_data['Problem Description'] = incoming_data['problem_description']
    incoming_data.drop(columns=['problem_description'], inplace=True)

    predictions = pipeline.predict(incoming_data['Problem Description'])
    return predictions

def predict(request):
    if request.method == 'POST':
        data = request.POST
        age = data['age']
        gender = data['gender']
        problem_description = data['problem_description']
        op1 = make_predictions_on_incoming_dataset({"age":age,"gender":gender,"problem_description":problem_description}, test)
        op3 = op1
        op1 = tuple(op1[0][0:3])
        icd10_pred, treatment_pred = predict_input(op1)
        print(icd10_pred)
        print(treatment_pred)
        api_url = 'http://icd10api.com/'
        params = {
            's': 'F42.2',
            'desc': 'short',
            'r': 'json'
        }
        # response = requests.get(api_url, params=params)
        # if response.status_code == 200:
        #     # Extract relevant data from the response
        #     api_data = response.json()
        #     # return (HttpResponse(str(api_data)))
        # # Render the results template with dynamic data
        return render(request, 'templates/results.html', {
            'icd_10_code': icd10_pred,
            'recommended_treatment': treatment_pred,
            'problem_summary': op1[0],
            'problem_category': op1[1],
            'psychological_category': op1[2],
        })

        # Redirect to the results page
        # return redirect('results')  # You can uncomment this line if you want to redirect
        
        # If you want to pass data through redirect, you can use query parameters
        # return redirect(f'/results/?icd_10_code={icd10_pred}&recommended_treatment={treatment_pred}&problem_summary={op1[0]}&problem_category={op1[1]}&psychological_category={op1[2]}')
    
    return render(request, 'templates/inputPage.html') 
    
        
    
    
