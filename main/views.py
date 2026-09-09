from django.shortcuts import render

from main.models import Experience


def show_main(request):
    context = {
        "name": "Nabila",
        "npm": "2506593613",
        "study_program": "S1 Ilmu Komputer",
        "bio": (
            "CS student at Universitas Indonesia, currently exploring my interests in data science and cybersecurity. I'm a quiet thinker who prefers observing, analyzing, and solving problems behind the scenes."
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Nabila",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)