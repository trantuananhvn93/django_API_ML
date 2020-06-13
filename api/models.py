from django.db import models

# Create your models here.
class car(models.Model):
    make =  models.FloatField(default=0)
    enginesize = models.FloatField(default=0)
    cylinders = models.FloatField(default=0)
    horsepower = models.FloatField(default=0)
    mpgcity = models.FloatField(default=0)
    mpghighway = models.FloatField(default=0)
    weight = models.FloatField(default=0)
    wheelbase = models.FloatField(default=0)
    length = models.FloatField(default=0)