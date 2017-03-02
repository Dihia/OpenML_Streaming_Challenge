from django.http import HttpResponse
from django.shortcuts import render
from .models import Contact


variables = {
    "title" : "Streaming Challenges - Tasks",
    "pageName" : "Tasks"
}

def index(request):
    task_list = Contact.objects.all()
    variables['task_list'] = task_list
    return render(request, 'tasks/index.html', variables)
