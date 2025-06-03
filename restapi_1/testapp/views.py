from django.shortcuts import render
import json ,io
from django.views.generic import View
from rest_framework.parsers import JSONParser
from testapp.models import Employee
from testapp.serialization import EmployeeSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
@method_decorator(csrf_exempt,name='dispatch')
class EmployeeCRUDCBV(View):
    def delete(self,request):
        json_data=request.body
        stream=io.BytesIO(json_data)
        pdata=JSONParser().parse(stream)
        id=pdata.get('id')
        emp=Employee.objects.get(id=id)
        emp.delete()
        msg={'msg':'resource delted sucessfully.....'}
        json_data=JSONRenderer().render(msg)
        return HttpResponse(json_data,content_type='application/json')

    def put(self,request):
        json_data=request.body
        stream=io.BytesIO(json_data)
        pdata=JSONParser().parse(stream)
        id=pdata.get('id',None)
        emp=Employee.objects.get(id=id)
        serializer=EmployeeSerializer(emp,data=pdata,partial=True)
        if serializer.is_valid():
            serializer.save()
            msg={'msg':'Resource updated successfully.....'}
            json_data=JSONRenderer().render(msg)
            return HttpResponse(json_data,content_type='application/json')
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json',status=400)
    def post(self,request):
        json_data=request.body
        stream=io.BytesIO(json_data)
        pdata=JSONParser().parse(stream) 
        serializer=EmployeeSerializer(data=pdata)
        if serializer.is_valid():
            serializer.save()
            msg = {'msg':'Resource created successfully.....'}
            json_data=JSONRenderer().render(msg)
            return HttpResponse(json_data,content_type='application/json')
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json',status=400)
    def get(self,request):
        json_data=request.body
        stream=io.BytesIO(json_data)
        pdata=JSONParser().parse(stream)
        id=pdata.get('id',None)
        if id is not None:
            emp=Employee.objects.get(id=id)
            serialiser=EmployeeSerializer(emp)
            json_data=JSONRenderer().render(serialiser.data)
            return HttpResponse(json_data,content_type='appliction/json')
        emp_all=Employee.objects.all()
        eserialiser=EmployeeSerializer(emp_all,many=True)
        json_data=JSONRenderer().render(eserialiser.data)
        return HttpResponse(json_data,content_type='application/json')

# Create your views here.
