from django.shortcuts import render
from django.http import HttpResponse
#create data without json by using the html respone
def emp_data_view(request):
    emp_data={
        'eno':1001,
        'ename':'jhon',
        'esal':10000,
        'eaddr':'hyd'
    }
    resp=' <h1>emplyeeno:{}<br>emplyeename:{}<br>emplyeesal:{}<br>emplyeeaddr:{}</h1>'.format(emp_data['eno'],emp_data['ename'],emp_data['esal'],emp_data['eaddr'])
    return HttpResponse(resp)#(resquerst--->resp)
#now we are gooing through the jsondata for api
import json
def emp_data_view1(request):
    emp_data={
        'eno':1001,
        'ename':'jhon',
        'esal':10000,
        'eaddr':'hyd'
    }
    json_data=json.dumps(emp_data)
    return HttpResponse(json_data,content_type='application/json')#(resquerst--->resp)
    # Create your views here.
