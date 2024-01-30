from django.shortcuts import render

# Create your views here.
# import viewsets
from rest_framework import viewsets
 
# import local data
from .serializers import GeeksSerializer
from .models import Employee
 
# create a viewset
 
 
class GeeksViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = Employee.objects.all()
 
    # specify serializer to be used
    serializer_class = GeeksSerializer