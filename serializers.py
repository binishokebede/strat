from rest_framework import serializers
 
# import model from models.py
from .models import Employee
 
# Create a model serializer
class GeeksSerializer(serializers.HyperlinkedModelSerializer):
    # specify model and fields
    class Meta:
        model = Employee
        fields = ('fullname', 'mobile')