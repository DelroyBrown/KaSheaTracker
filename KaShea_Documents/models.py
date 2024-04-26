from django.db import models


class Document(models.Model):
    file_name = models.CharField(blank=False, null=False, max_length=100, default="")
    file_upload = models.FileField(upload_to="documents/")
    description = models.TextField(blank=False, null=False, max_length=2000, default="")
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.file_name}"

    class Meta:
        ordering = ["-upload_date"]
