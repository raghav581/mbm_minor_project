from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import json
import pickle
import numpy
from .utils import get_price_from_model
class getListCities(APIView):
	def get(self,request,*args,**kwargs):
		ans=['nitin','saini']
		with open("columns.json",'r') as f:
			locations = json.load(f)
		return Response(locations)
	
class predictPrice(APIView):
	def post(self,request,*args,**kwargs):
		area= request.data.get('area')
		bath=request.data.get('bathroom')
		bhk=request.data.get('bhk')
		location=request.data.get('location')
		availibility=request.data.get('availability')
		area_type=request.data.get('type')
		print(area,bath,bhk,location,availibility,area_type)
		ans=get_price_from_model(area=1056.0,bhk=2,bath=2,availibility='Ready To Move',area_type='Built-up  Area',location=' Devarachikkanahalli')
		return Response({'price':ans})
def home(request):
	if request.method=='POST':
		area=request.POST['area']
		bath=request.POST['bathroom']
		bhk=request.POST['bhk']
		location=request.POST['location']
		bavailabilityhk=request.POST['availability']
		location=request.POST['type']
		
		return render(request,'home.html',{"ans":127465})
	else:
		return render(request,'home.html')


# area
# bhk
# bathrooms
# location
# availability->ready
# area_type
# price

