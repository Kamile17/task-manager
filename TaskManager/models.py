from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User


class Task(models.Model):
    task_title = models.CharField(max_length=200, null=True)
    task_description = models.TextField(max_length=3000, null=True)
    assigned_to = models.ManyToManyField(User, through="AssignedTask", through_fields=('task', 'user'))
    date_created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="created_by", null=True, blank=True)
    due_date = models.DateTimeField(blank=False)

    def __str__(self):
        return str(self.task_title)


class AssignedTask(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, null=True, default="not_completed")
    date_completed = models.DateTimeField(null=True, blank=True)
    assigned_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="assigned_by")


    class Meta:
        unique_together = ('user', 'task')

    def __str__(self):
        s = f'{self.task.task_title} - {self.user.first_name} {self.user.last_name}'
        return str(s)
