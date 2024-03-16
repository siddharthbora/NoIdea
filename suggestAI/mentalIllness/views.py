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



def home(request):
    return render(request, 'templates/landingPage.html')

def listing(request):
    return render(request, 'templates/ListingPage.html')



encoder, tfidf_vectorizer, rf_icd10, rf_treatment = joblib.load("/Users/siddharth/Desktop/Hackathon DI/suggestAI/mentalIllness/medical_predictor_model2.pkl")

def predict_input( input_tuple):
    input_data = pd.DataFrame([input_tuple], columns=['Problem Summary', 'Problem Category', 'Psychological Category'])

    input_encoded = encoder.transform(input_data[['Problem Category', 'Psychological Category']])
    input_summary = tfidf_vectorizer.transform(input_data['Problem Summary'])
    input_combined = hstack((input_encoded, input_summary))

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
        return render(request, 'templates/results.html', {
            'icd_10_code': icd10_pred,
            'recommended_treatment': treatment_pred,
            'problem_summary': op1[0],
            'problem_category': op1[1],
            'psychological_category': op1[2],
        })
    return render(request, 'templates/inputPage.html') 
    
        
    
    
