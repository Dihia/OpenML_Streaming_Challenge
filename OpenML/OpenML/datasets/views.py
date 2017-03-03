from django.http import HttpResponse
from django.shortcuts import render
import json
from os import walk

variables = {
    "title" : "Streaming Challenges - Datasets",
    "pageName" : "Datasets"
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
    "task_id": 23,
    "nb_runs": 0,
    "nb_likes": 1,
    "nb_downloads": 2,
    "nb_reachs": 3,
    "nb_impacts": 4,
    "dataset_id": 23,
    "dataset_name": " molecular-biology_promoters"
}

with open('/home/colette/creations/openml/OpenML_Streaming_Challenge/OpenML/OpenML/datasets/dataset.json') as data_file:
    dataset = json.load(data_file)



tasks = {
    123: task_example1,
    23 : task_example
}


def index(request):

    dataset_list = [dataset]
    variables['datasets'] = dataset_list

    return render(request, 'datasets/index.html', variables)

def show(request,id):
    #get the dataset of the id
    variables['dataset'] = dataset
    #list all tasks of this datasets
    variables['tasks'] = [task_example,task_example1]

    return render(request,'datasets/show.html',variables)