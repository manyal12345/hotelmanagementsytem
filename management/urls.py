from django.urls import path
from management.views import EnmloyeeInfoView

urlpatterns = [
    path('employee/', EnmloyeeInfoView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='employee'),
]