from django.shortcuts import render, redirect
from .models import Tasks
from .forms import TaskForm


def tasks(request):
    all_tasks = Tasks.objects.all().order_by(
        "-date_added"
    )
    return render(request, "KaShea_Tasks/tasks.html", {"tasks": all_tasks})


def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("KaShea_Tasks:tasks")
    else:
        form = TaskForm()
    return render(request, "KaShea_Tasks/create_task.html", {"form": form})


