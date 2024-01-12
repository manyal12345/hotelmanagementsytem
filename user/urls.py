from django.urls import path
from user.views import group_list, login, owner_create

urlpatterns = [
    path('login/',login,name='login'),
    path('group/all/',group_list,name='group'),
    path('owner-create/',owner_create,name='owner-create'),
]
