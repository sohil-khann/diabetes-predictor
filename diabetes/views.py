import os
from django.contrib import messages
from django.shortcuts import render, redirect
import pandas as pd
import pickle
from .models import DiabeticPrediction



def predict(request):
    if request.method == 'POST':
        Name = request.POST['Name']
        gender = request.POST['gender']
        age = float(request.POST['age'])
        hypertension = int(request.POST.get('hypertension', 0))
        heart_disease = int(request.POST.get('heart_disease', 0))
        smoking_history = request.POST['smoking_history']
        bmi = float(request.POST['bmi'])
        HbA1c_level = float(request.POST['HbA1c_level'])
        blood_glucose_level = float(request.POST['blood_glucose_level'])
        
        model_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'diabetes_model.pkl')
        with open(model_path, 'rb') as f:
            model = pickle.load(f)
       
        import numpy as np
        input_data = pd.DataFrame({
            'gender': [gender],
            'age': [float(age)],
            'hypertension': [int(hypertension)],
            'heart_disease': [int(heart_disease)],
            'smoking_history': [smoking_history],
            'bmi': [float(bmi)],
            'HbA1c_level': [float(HbA1c_level)],
            'blood_glucose_level': [float(blood_glucose_level)]
        })
        
        result = model.predict(input_data)
        
        print(result)
        is_diabetic = result[0]
        
        ins = DiabeticPrediction(
            Name=Name,
            gender=gender,
            age=age,
            hypertension=bool(hypertension),
            heart_disease=bool(heart_disease),
            smoking_history=smoking_history,
            bmi=bmi,
            HbA1c_level=HbA1c_level,
            blood_glucose_level=blood_glucose_level,
            is_diabetic=is_diabetic
        )
        ins.save()
        
        context = {
            'Name': Name,
            'gender': gender,
            'age': age,
            'hypertension': hypertension,
            'heart_disease': heart_disease,
            'smoking_history': smoking_history,
            'bmi': bmi,
            'HbA1c_level': HbA1c_level,
            'blood_glucose_level': blood_glucose_level,
            'final': is_diabetic
        }
        return render(request, 'index.html', context)
    return render(request, 'index.html')


def results(request):
    preds = DiabeticPrediction.objects.all()
    context = {'preds': preds}
    return render(request, 'results.html', context)


def delete(request):
    predss = DiabeticPrediction.objects.all()
    predss.delete()
    return redirect('/')
