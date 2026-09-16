from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from main.forms import *
from main.models import *
from portofolio import settings


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
        "education_list": Education.objects.all(),
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

def show_skill(request):
    context = {
        "first_name": "Nabila",
        "middle_name": "Oktavia",
        "last_name": "Ramadhani",
        "skill_list": Skill.objects.all(),
    }
    return render(request, "skill.html", context)

def show_projects(request):
    json_response = get_projects_json(request)

    projects = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    projects = [project.object for project in projects]
    title_query = request.GET.get("title", "").strip()

    context = {
        "first_name": "Nabila",
        "middle_name": "Oktavia",
        "last_name": "Ramadhani",
        "project_list": projects,
        "title_query": title_query,
    }
    return render(request, "project.html", context)

def create_project(request):
    form = ProjectForm(request.POST or None)

    if request.method == "POST":
        header_key = request.headers.get("X-Secret-Key")
        form_key = request.POST.get("secret_key")
        submitted_key = header_key or form_key

        if submitted_key != settings.PORTFOLIO_SECRET_KEY:
            messages.error(request, "Kode rahasia salah! Kamu tidak punya akses untuk menambah proyek.")
            return redirect("main:create_project")

        if form.is_valid():
            form.save()
            messages.success(request, "Proyek baru berhasil ditambahkan!")
            return redirect("main:show_projects")

    context = {
        "first_name": "Nabila",
        "middle_name": "Oktavia",
        "last_name": "Ramadhani",
        "form": form,
    }
    return render(request, "projects_form.html", context)

def get_projects_json(request):
    title_query = request.GET.get("title", "").strip()
    projects = Project.objects.all()

    if title_query:
        projects = projects.filter(title__icontains=title_query)

    projects_json = serializers.serialize("json", projects)
    return HttpResponse(projects_json, content_type="application/json")

def delete_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        # Cek secret key dulu
        header_key = request.headers.get("X-Secret-Key")
        form_key = request.POST.get("secret_key")
        submitted_key = header_key or form_key

        if submitted_key != settings.PORTFOLIO_SECRET_KEY:
            messages.error(request, "Kode rahasia salah! Kamu tidak punya akses untuk menghapus proyek.")
            return redirect("main:show_projects")

        project.delete()
        messages.success(request, "Project berhasil dihapus!")
        return redirect("main:show_projects")

    return redirect("main:show_projects")