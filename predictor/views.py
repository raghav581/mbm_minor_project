from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

class getListCities(APIView):
	def get(self,request,*args,**kwargs):
		ans=['nitin','saini']
		return Response(ans)


def home(request):
	if request.method=='POST':
		name=request.POST['name']
		return render(request,'Jodhpur.html',{"ans":name})
	else:
		return render(request,'Jodhpur.html')