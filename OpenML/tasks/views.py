from django.http import HttpResponse
from django.shortcuts import render


from openml import tasks

task_list = [tasks.get_task(9)]



def get(request):
    return render(request, 'tasks.html', {'tasks': task_list})

