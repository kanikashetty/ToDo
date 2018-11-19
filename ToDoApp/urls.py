from django.urls import path,re_path
from . import views

urlpatterns = [
    path('',views.listToDo, name='listToDo'),
    path('addToDo',views.addToDo, name='addToDo'),
    re_path(r'^updateToDo/(?P<title>.*)$',views.updateToDo, name='updateToDo'),
    re_path(r'^deleteToDo/(?P<title>.*)$',views.deleteToDo, name='deleteToDo'),
    re_path(r'^listToDoapi/(?P<title>.*)$',views.listToDoapi, name='listToDoapi')
]