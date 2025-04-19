from django.db import models


# Create your models here.


class DiabeticPrediction(models.Model):
    Name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10, choices=[
        ('Male', 'Male'),
        ('Female', 'Female')
    ])
    age = models.FloatField()
    hypertension = models.BooleanField(default=False)
    heart_disease = models.BooleanField(default=False)
    smoking_history = models.CharField(max_length=20, choices=[
        ('never', 'Never'),
        ('former', 'Former'),
        ('current', 'Current'),
        ('No Info', 'No Info')
    ])
    bmi = models.FloatField()
    HbA1c_level = models.FloatField()
    blood_glucose_level = models.FloatField()
    is_diabetic = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.Name
