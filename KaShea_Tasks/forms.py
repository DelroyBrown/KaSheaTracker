from django import forms
from .models import Tasks


class TaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = [
            "task_name",
            "task_description",
            "due_date",
            "priority",
            "category",
            "reminder_date",
            "assigned_to",
        ]
        widgets = {
            "task_name": forms.TextInput(attrs={"class": "form-control"}),
            "task_description": forms.Textarea(attrs={"class": "form-control"}),
            "due_date": forms.DateInput(
                format=("%Y-%m-%d"), attrs={"class": "form-control", "type": "date"}
            ),
            "priority": forms.Select(attrs={"class": "form-control"}),
            "category": forms.TextInput(attrs={"class": "form-control"}),
            "reminder_date": forms.DateTimeInput(
                format=("%Y-%m-%d %H:%M"),
                attrs={"class": "form-control", "type": "datetime-local"},
            ),
            "assigned_to": forms.TextInput(attrs={"class": "form-control"}),
        }
