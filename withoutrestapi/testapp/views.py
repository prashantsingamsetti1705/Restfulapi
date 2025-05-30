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
from django.views.generic import View
class emp_data_view2(View):
    def get(self,request):
        empdata={
            'en0':1001,
            'ename':'jhon',
            'easl':10000,
            'eddar':'hyd'
        }
        json_data=json.dumps(empdata)
        return HttpResponse(json_data,content_type='application/json'
                            )
# # now we are going work with  post,pust,delete
# class emp_data_view3(View):
#     def put(self,request):
#         json_data=json.dumps({'msg':'put method is called'})
#         return HttpResponse(json_data,content_type='application/json')
# class emp_data_view4(View):
#     def post(self,request):
#         json_data=json.dumps({'msg':'post method is called'})
#         return HttpResponse(json_data,content_type='application/json')
# class emp_data_view5(View):
#     def delete(self,request):
#         json_data=json.dumps({'msg':'delete method is called'})
#         return HttpResponse(json_data,content_type='application/json')