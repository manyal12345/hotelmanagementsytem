from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from management.models import EmployeeInfo
from management.serializers import EmployeeInfoSerializer
from user.models import User
from user.serializers import UserSerializer
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from rest_framework.filters import SearchFilter

# Create your views here.

class EnmloyeeInfoView(ModelViewSet):
    queryset = EmployeeInfo.objects.all()
    serializer_class = EmployeeInfoSerializer
    filter_backends = [SearchFilter]
    search_fields =  ['name', 'number']

    def create(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        hash_password = make_password(password)
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                user = User.objects.create_user(email=email, password=hash_password)
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        else:
            return Response(serializer.errors)