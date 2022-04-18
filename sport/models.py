from django.db import models

from django.utils.timezone import now


class Biking(models.Model):
    date = models.DateTimeField(default=now, null=True, blank=True)
    resistance = models.IntegerField(default=0, blank=True, null=True)


class BikePartialExercise(models.Model):
    date = models.DateTimeField(auto_now_add=True, null=True)


class Dumbbell(models.Model):
    date = models.DateTimeField(default=now)
    weight = models.IntegerField(default=15)


class Abdo(models.Model):
    date = models.DateTimeField(default=now)
