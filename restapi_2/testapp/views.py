from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

class TestapiView(APIView):
    def get(self,request):
        data={
            'name':'testapi',
            'description':'this is atest api view',
            'status':'sucess'
        }
        return Response({'msg':'this is a test api view','data':data})
    def post(self,request):
        return Response({'msg':'this is a test api view'})
    def put(self,request):
        return Response({'msg':'this is a test api view'})
    def delete(self,request):
        return Response({'msg':'this is a test api view'})

    
# Create your views here.
