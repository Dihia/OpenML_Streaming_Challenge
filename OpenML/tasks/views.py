from django.http import HttpResponse
from django.shortcuts import render


from openml import tasks

task = tasks.get_task(1)

task_list = [task]

def index(request):
    return render(request, 'tasks.html', {'tasks': task_list})
