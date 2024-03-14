from django.shortcuts import render

from main import models


def index(request):
    return render(
        request,
        "main/index.html",
        {
            "place_list": models.Place.objects.all(),
        },
    )
