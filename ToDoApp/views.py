from django.shortcuts import render
from django.http import HttpResponseRedirect,JsonResponse
from django.urls import reverse
from django.contrib import messages
from django.utils.timezone import localtime
from ToDoApp.models import ToDoList

import json
import logging
import datetime

logger = logging.getLogger(__name__)

def listToDo(request):
    " view to list all the ToDo."
    try:
        if request.method == "GET":
            ToDo_list = ToDoList.objects.all()
            return render(request,'ToDoApp/ToDoList.html',context = {'ToDo_list' : ToDo_list })
    except Exception as e:
        logger.exception(e)

def addToDo(request):
    "View to Add ToDo List"
    try:
        if request.method == "POST":
            addToDo =  ToDoList()
            addToDo.Title = request.POST.get('title')
            addToDo.Description = request.POST.get('description')
            addToDo.Deadline_Date = request.POST.get('deadline')
            addToDo.Status = request.POST.get('status')
            # addToDo.CreatedAt = request.POST.get('expense_currency')
            # addToDo.ModifiedAt = request.POST.get('expense')
            
            addToDo.save()
            return HttpResponseRedirect(reverse('listToDo'))
        elif request.method == "GET":
            #print("client_name:",client_name)
            return render(request,'ToDoApp/addToDo.html')
    except Exception as e:
        messages.error(request,'Something went wrong!')
        logger.exception(e)
        return render(request,'ToDoApp/addToDo.html')

def updateToDo(request,title):
    "View to Update the ToDo List"
    try:
        if request.method == "POST":
            updateToDo =  ToDoList.objects.get(Title=title)
            updateToDo.Description = request.POST.get('description')
            updateToDo.Deadline_Date = request.POST.get('deadline')
            updateToDo.Status = request.POST.get('status')
            updateToDo.save()
            return HttpResponseRedirect(reverse('listToDo'))
        elif request.method == "GET":
            detailToDo = ToDoList.objects.get(Title=title)
            time = localtime(detailToDo.Deadline_Date).strftime("%Y-%m-%dT%H:%M:%S")
            detailToDo.Deadline_Date = time
            return render(request,'ToDoApp/updateToDo.html',context={"detailToDo":detailToDo})
    except Exception as e:
        messages.error(request,'Something went wrong!')
        logger.exception(e)
        return render(request,'ToDoApp/updateToDo.html')

def deleteToDo(request,title):
    "View to Delete the ToDo List"
    try:
        ToDoList.objects.get(Title=title).delete()
        return HttpResponseRedirect(reverse('listToDo'))
    except Exception as e:
        messages.error(request,'Something went wrong!')
        logger.exception(e)
        return render(request,'ToDoApp/listToDo.html')
        
def listToDoapi(request,title):
    " view to get list of ToDo as api"
    try:
        if title:
            ToDo_api = {}
            ToDo_list = ToDoList.objects.get(Title=title)
            ToDo_api["Title"] = ToDo_list.Title
            ToDo_api["Description"] = ToDo_list.Description
            ToDo_api["Deadline_Date"] = ToDo_list.Deadline_Date
            ToDo_api["Status"] = ToDo_list.Status
            ToDo_api["CreatedAt"] = ToDo_list.CreatedAt
            ToDo_api["ModifiedAt"] = ToDo_list.ModifiedAt
            return JsonResponse(ToDo_api)
        else:
            ToDo_list = ToDoList.objects.all()
            ToDo_api_list = []
            ToDo_api = {}
            for item in ToDo_list:
                ToDo_api["Title"] = item.Title
                ToDo_api["Description"] = item.Description
                ToDo_api["Deadline_Date"] = item.Deadline_Date
                ToDo_api["Status"] = item.Status
                ToDo_api["CreatedAt"] = item.CreatedAt
                ToDo_api["ModifiedAt"] = item.ModifiedAt
                ToDo_api_list.append(ToDo_api)
            return JsonResponse(ToDo_api_list, safe=False)
    except Exception as e:
        logger.exception(e)
    
