from django.contrib import admin
from .models import DiabeticPrediction


# Register your models here.
class DiabeticAdmin(admin.ModelAdmin):
    list_display = ('Name', 'gender', 'age', 'hypertension', 'heart_disease', 'smoking_history', 'bmi', 'HbA1c_level', 'blood_glucose_level', 'is_diabetic')


admin.site.register(DiabeticPrediction, DiabeticAdmin)
