# Diabetes Prediction System

## Project Overview
A Django-based web application that predicts diabetes risk using machine learning. Integrates a pre-trained model with clinical data parameters stored in MongoDB.
-  ML Algo.: Logistic regression, Random Forest Classifier, Naïve Bayes and other Data Pre-processing, testing algorithms.
-  Dataset:  Diabetes Prediction Datase
t
# Check Dataset or ML model from "lab2.pdf" f

## Features
- Risk prediction using 8 health parameters
- Persistent storage of predictions
- Results visualization
- Data management interface

## Installation
```bash
pip install -r requirements.txt
```

## Configuration
1. Install MongoDB Community Edition
2. Update DATABASES in settings.py:
```python
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'diabetes_db',
        'CLIENT': {
            'host': 'mongodb://localhost:27017/',
        }
    }
}
```

## Dataset
Model trained on [Diabetes Prediction Dataset](https://www.kaggle.com/datasets/iammustafatz/diabetes-prediction-dataset)

## Model Integration
1. Place diabetes_model.pkl in project root
2. Model automatically loads on server start

## Usage
```bash
python manage.py migrate
python manage.py runserver
```

## API Endpoints
- `/` - Prediction form
- `/results` - Historical predictions
- `/delete` - Clear all records

## Dependencies
- Django 3.1.12
- Scikit-learn 1.0.2
- Pandas 1.3.5
- Djongo 1.3.6
