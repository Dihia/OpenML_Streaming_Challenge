from django.http import HttpResponse
from django.shortcuts import render


from openml import tasks

#task_list = [tasks.get_task(2056)]
task_list_id= tasks.list_tasks(task_type_id=9)
task_list=[]

for id in task_list_id:
    try:
        task_list.append(tasks.get_task(id))
    except:
        pass




def get(request):
    return render(request, 'tasks.html', {'tasks': task_list_id})

