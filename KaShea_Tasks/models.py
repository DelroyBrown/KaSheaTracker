from django.db import models


class Tasks(models.Model):
    HIGH = "High"
    MEDIUM = "Medium"
    LOW = "Low"
    PRIORITY_CHOICES = [
        (HIGH, "High"),
        (MEDIUM, "Medium"),
        (LOW, "Low"),
    ]

    task_name = models.CharField(max_length=100, default="")
    task_description = models.TextField(max_length=2000, default="")
    due_date = models.DateField()
    completion_status = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True)
    priority = models.CharField(max_length=6, choices=PRIORITY_CHOICES, default=MEDIUM)
    category = models.CharField(max_length=100, default="General")
    reminder_date = models.DateTimeField(null=True, blank=True)
    assigned_to = models.CharField(max_length=100, default="Karissa", blank=True)

    def __str__(self):
        return f"{self.task_name}"
