from __future__ import unicode_literals

from django.db import models

class Task(models.Model):
    task_id = models.IntegerField(default=9)
    task_type= models.CharField(max_length=200)
    dataset_id = models.IntegerField(default=1)

