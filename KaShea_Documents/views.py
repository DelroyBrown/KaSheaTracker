from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Document
from .forms import DocumentForm


def upload_documents(request):
    if request.method == "POST":
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("KaShea_Documents:documents")
    else:
        form = DocumentForm()
    return render(request, "KaShea_Documents/upload.html", {"form": form})


def documents(request):
    documents = Document.objects.all().order_by(
        "-upload_date"
    )
    return render(request, "KaShea_Documents/documents.html", {"documents": documents})
