from django.http import HttpResponse
from openml import tasks,datasets


def index(request):
    task = tasks.get_task(9)
    data = datasets.get_dataset(244)
    #r=requests.get("http://www.openml.org/api/v1/task/9?key_api = a2ac595c56b398c8db7a4be791db9083")
    return HttpResponse(str(task.task_id))