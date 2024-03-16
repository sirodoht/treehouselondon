from django.db import models


class Place(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100, unique=True)
    url = models.URLField("URL")
    borough = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.id}: {self.name}"
