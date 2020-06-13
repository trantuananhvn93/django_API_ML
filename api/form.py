from django import forms

class CarForm(forms.Form):
    make = forms.FloatField()
    enginesize = forms.FloatField()
    cylinders = forms.FloatField()
    horsepower = forms.FloatField()
    mpgcity = forms.FloatField()
    mpghighway = forms.FloatField()
    weight = forms.FloatField()
    wheelbase = forms.FloatField()
    length = forms.FloatField()
