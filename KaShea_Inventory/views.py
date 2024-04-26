from django.shortcuts import render

def inventory(request):
    return render(request, 'KaShea_Inventory/inventory.html')