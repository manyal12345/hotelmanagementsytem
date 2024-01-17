from django.shortcuts import render
from rest_framework.decorators import api_view
from accounting.models import Bill, Payment
from rest_framework.response import Response
from rest_framework.permissions import DjangoModelPermissions
from accounting.serializers import BillSerializer, PaymentSerializer
from rest_framework.viewsets import ModelViewSet
from core.premission import CustomPremission
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
# Create your views here.
# @api_view(['GET'])
# def bill_view(request):
#     bill_obj = Bill.objects.all()
#     bill_json = BillSerializer(bill_obj, many=True)
#     return Response(bill_json.data)

class BillView(ModelViewSet):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer
    permission_classes = [CustomPremission]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['guest']
    search_fields = ['amount']

    def list(self, request):
        querryset = self.get_queryset()
        filter_querryset = self.filter_queryset(querryset)
        serializer = self.serializer_class(filter_querryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def retrieve(self, request, pk=None):
        # querryset = self.get_queryset()
        # bill_obj = querryset.get(id=pk)
        # serializer = self.serializer_class(bill_obj)
        # return Response(serializer.data)
        try:
            queryset = Bill.objects.get(id=pk)
        except:
            return Response({"error": "Bill not found"})
        serializer = self.serializer_class(queryset)
        return Response(serializer.data)


    def update(self, request, pk=None):
        try:
            queryset = Bill.objects.get(id=pk)
        except:
            return Response({"error": "Bill not found"})
        serializer = self.serializer_class(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def destroy(self, request, pk=None):
        try:
            queryset = Bill.objects.get(id=pk)
        except:
            return Response({"error": "Bill not found"})
        queryset.delete()
        return Response({"message": "Bill deleted"})