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
    "nb_impacts": 4,
    "dataset_id": 44,
    "dataset_name": "spambase"
}

task_example = {
    "name": "Supervised Data Stream Classification on molecular-biology_promoters",
    "id": 23,
    "nb_runs": 0,
    "nb_likes": 1,
    "nb_downloads": 2,
    "nb_reachs": 3,
    "nb_impacts": 4,
    "dataset_id": 23,
    "dataset_name": " molecular-biology_promoters"
}

tasks = {
    123: task_example1,
    23 : task_example
}


def index(request):

    task_list = [task_example,task_example1]
    variables['tasks'] = task_list

    return render(request, 'tasks/index.html', variables)

def show(request,id):
    variables['task'] = tasks[int(id)]

    return render(request,'tasks/show.html',variables)