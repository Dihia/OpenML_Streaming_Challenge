from django.http import HttpResponse
from django.shortcuts import render
from .models import Contact


variables = {
    "title" : "Streaming Challenges - Tasks",
    "pageName" : "Tasks"
}

task_example1 = {
    "name": "Supervised Data Stream Classification on blabal",
    "id": 123,
    "nb_runs": 0,
    "nb_likes": 1,
    "nb_downloads": 2,
    "nb_reachs": 3,
    "nb_impacts": 4
}

task_example = {
    "name": "Supervised Data Stream Classification on molecular-biology_promoters",
    "id": 23,
    "nb_runs": 0,
    "nb_likes": 1,
    "nb_downloads": 2,
    "nb_reachs": 3,
    "nb_impacts": 4
}

def index(request):

    task_list = [task_example,task_example1]
    variables['tasks'] = task_list

    return render(request, 'tasks/index.html', variables)

def show(request):

    variables['task'] = task_example
    return render(request,'tasks/show.html',variables)