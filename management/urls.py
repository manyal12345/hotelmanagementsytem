from django.urls import path
from management.views import EnmloyeeInfoView

urlpatterns = [
    path('employee-info/all/', EnmloyeeInfoView.as_view({'get': 'list', 'post': 'create', 'put': 'update', 'delete': 'destroy'}), name='employee'),
]