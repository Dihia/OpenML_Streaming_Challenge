from __future__ import unicode_literals

from django.db import models
from openml import tasks


# Create your models here.
#class Task(models.Model):
#    task_id = tasks.get_task(1).task_id


class Contact(models.Model):

    first_name = models.CharField(
        max_length=255,
    )
    last_name = models.CharField(
        max_length=255,

    )

    email = models.EmailField()

    def __str__(self):

        return ' '.join([
            self.first_name,
            self.last_name,
        ])