from django.shortcuts import render

def reports(request):
    return render(request, 'KaShea_Reports/reports.html')