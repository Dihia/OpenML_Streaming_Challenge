from django.http import HttpResponse
from django.shortcuts import render


from openml import tasks

task = tasks.get_task(1)
from django.shortcuts import render


def index(request):


    return render(request, 'tasks.html', {'tasks': [task]})
