from django.db import models


class ToDo(models.Model):
    task_name = models.CharField(blank=False, null=False, max_length=100, default="")
    task_description = models.TextField(
        blank=False, null=False, max_length=2000, default=""
    )
    due_date = models.DateField()
    completion_status = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.task_name}"
