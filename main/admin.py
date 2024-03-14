from django.contrib import admin

from main import models


@admin.register(models.Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "url",
        "borough",
        "member_count",
        "created_at",
        "updated_at",
    )
    search_fields = ("name", "url", "borough")
    ordering = ["-id"]
