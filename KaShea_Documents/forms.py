from django import forms
from .models import Document


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = [
            "file_name",
            "file_upload",
            "description",
            # "upload_date",
        ]
