from django.http import HttpResponse
from django.shortcuts import render
from .models import Contact

def index(request):
    task_list = Contact.objects.all()
    return render(request, 'tasks/index.html', {'tasks': task_list})
