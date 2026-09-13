from django.shortcuts import render

from main.models import Experience


def show_main(request):
    context = {
        "first_name": "Nabila",
        "middle_name": "Oktavia",
        "last_name": "Ramadhani",
        "npm": "2506593613",
        "major": "S1 Ilmu Komputer",
        "bio": (
            "CS student at Universitas Indonesia, currently exploring my interests in data science and cybersecurity. I'm a quiet thinker who prefers observing, analyzing, and solving problems behind the scenes."
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "first_name": "Nabila",
        "middle_name": "Oktavia",
        "last_name": "Ramadhani",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)