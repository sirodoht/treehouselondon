from django.db import models


class Place(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100)
    url = models.URLField("URL")
    member_count = models.PositiveSmallIntegerField()
    borough = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.id}: {self.name}"
