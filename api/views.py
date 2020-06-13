from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from django.http import JsonResponse
from .serializers import carSerializers
from .models import car
from .form import CarForm
import pandas as pd
import numpy as np
import pickle
import os
from rest_framework.permissions import IsAuthenticated

# Load the Model back from file
with open('api/model.pkl', 'rb') as file:
    model = pickle.load(file)

def index(request):
	return render(request, 'index.html')


# @csrf_exempt
def submit(request):
	if request.method == 'POST':
		myDict = (request.POST).dict()
		df = pd.DataFrame(myDict, index=[0])
		df.drop('csrfmiddlewaretoken', axis=1, inplace=True)
		df = df.astype(float)
		x = df.to_numpy()[0].reshape(1,-1)
		y = model.predict(x)[0]
		context = {'price': y}
		return render(request, 'price.html', context)


	# def submitform(self, request, *args, **kwargs):

