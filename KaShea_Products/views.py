from django.shortcuts import render

def products(request):
    return render(request, 'KaShea_Products/products.html')