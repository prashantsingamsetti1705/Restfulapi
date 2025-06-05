from django.shortcuts import render
from testapp.models import Employee
from testapp.serializers import EmployeeSerializer
from rest_framework.views import View,APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView
class EmployeeCreatedAPIView(APIView):
    def get(self,request):
        qs=Employee.objects.all()
        serializer=EmployeeSerializer(qs,many=True)
        return Response(serializer.data)
class EmployeelistApiView(ListAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
class Employeeretrive(RetrieveAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    lookup_field="id"
class EmployeeUpdate(UpdateAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    lookup_field="id"
class EmployeeDelteView(DestroyAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    lookup_field="id"
# Create your views here.
