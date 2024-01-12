from django.shortcuts import render
from rest_framework import serializers
from management.models import EmployeeInfo

class EmployeeInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeInfo
        fields = '__all__'