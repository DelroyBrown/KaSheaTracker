from django.shortcuts import render


def tasks(request):
    return render(request, "KaShea_Tasks/tasks.html")
