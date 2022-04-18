from django.db import models

# Create your models here.
class BodyShape(models.Model):
    date = models.DateTimeField(unique=True)
    bmi = models.FloatField()
    weight = models.FloatField()
    body_fat = models.FloatField()
    muscle_mass = models.FloatField()
    visceral_fat = models.FloatField()
    body_water = models.FloatField()
    bone_mass = models.FloatField()
    bmr = models.FloatField()
    protein_rate = models.FloatField()
    skeletal_muscle_rate = models.FloatField()
    subcutaneous_fat = models.FloatField()
    lean_body_mass = models.FloatField()
