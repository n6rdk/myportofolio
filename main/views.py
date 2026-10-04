import datetime
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.exceptions import PermissionDenied
from django.views.decorators.http import require_POST
from main.forms import *
from main.models import *

def is_editor(user):
    return user.groups.filter(name="Editor").exists()

def show_main(request):
    last_login = request.COOKIES.get('last_login', 'No login session yet / Cookie not found')
    print("LAST LOGIN:", repr(last_login))
    
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
        "last_login": last_login,
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

@login_required(login_url="/login/")
def create_experience(request):
    if not request.user.is_superuser:
        raise PermissionDenied
    
    form = ExperienceForm(request.POST or None)
    
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, "New experience successfully added!")
            return redirect("main:show_experience")

    context = {
        "first_name": "Nabila",
        "middle_name": "Oktavia",
        "last_name": "Ramadhani",
        "form": form,
    }
    return render(request, "experience_form.html", context)

def get_experience_json(request):
    experiences = Experience.objects.all()
    experiences_json = serializers.serialize("json", experiences)
    return HttpResponse(experiences_json, content_type="application/json")

@login_required(login_url="/login/")
def delete_experience(request, experience_id):
    if not request.user.is_superuser:
        raise PermissionDenied
        
    experience = get_object_or_404(Experience, pk=experience_id)
    experience.delete()
    messages.success(request, "Experience successfully deleted!")
    return redirect("main:show_experience")

@login_required(login_url="/login/")
def edit_experience(request, experience_id):
    if not request.user.is_superuser:
        raise PermissionDenied
    
    experience = get_object_or_404(Experience, pk=experience_id)
    form = ExperienceForm(request.POST or None, instance=experience)
    
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Experience successfully updated!")
        return redirect("main:show_experience")

    context = {
        "first_name": "Nabila",
        "middle_name": "Oktavia",
        "last_name": "Ramadhani",
        "form": form,
        "experience": experience,
    }
    return render(request, "experience_form.html", context)

def show_skill(request):
    context = {
        "first_name": "Nabila",
        "middle_name": "Oktavia",
        "last_name": "Ramadhani",
        "skill_list": Skill.objects.all(),
    }
    return render(request, "skill.html", context)

def show_project(request):
    title_query = request.GET.get("title", "").strip()

    context = {
        "first_name": "Nabila",
        "middle_name": "Oktavia",
        "last_name": "Ramadhani",
        "title_query": title_query,
        "can_edit": request.user.is_authenticated and (
            is_editor(request.user) or request.user.is_superuser
        ),
        "form": ProjectForm(),
    }
    return render(request, "project.html", context)

@login_required(login_url="/login/")
def create_project(request):
    if not request.user.is_superuser:
        raise PermissionDenied
    
    form = ProjectForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, "New project successfully added!")
            return redirect("main:show_project")

    context = {
        "first_name": "Nabila",
        "middle_name": "Oktavia",
        "last_name": "Ramadhani",
        "form": form,
    }
    return render(request, "project_form.html", context)

@login_required(login_url="/login/")
def edit_project(request, project_id):
    if not (is_editor(request.user) or request.user.is_superuser):
            raise PermissionDenied
        
    project = get_object_or_404(Project, pk=project_id)
    form = ProjectForm(request.POST or None, instance=project)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, "Project successfully updated!")
            return redirect("main:show_project")

    context = {
        "first_name": "Nabila",
        "middle_name": "Oktavia",
        "last_name": "Ramadhani",
        "form": form,
        "project": project,
    }
    return render(request, "project_form.html", context)

@login_required(login_url="/login/")
def delete_project(request, project_id):
    if not request.user.is_superuser:
        raise PermissionDenied
        
    project = get_object_or_404(Project, pk=project_id)
    project.delete()
    
    messages.success(request, "Project successfully deleted!")
    return redirect("main:show_project")

def get_project_json(request):
    title_query = request.GET.get("title", "").strip()
    projects = Project.objects.prefetch_related('starred_by').all()

    if title_query:
        projects = projects.filter(title__icontains=title_query)

    # Konstruksi data JSON secara manual agar bisa menyisipkan logika Star
    data = []
    for project in projects:
        starred_users = project.starred_by.all()
        is_starred = request.user in starred_users if request.user.is_authenticated else False
        starred_by_names = ", ".join([u.username for u in starred_users])

        data.append({
            "pk": str(project.id),
            "fields": {
                "title": project.title,
                "description": project.description,
                "tech_stack": project.tech_stack,
                "project_url": project.project_url,
                "project_image_url": project.project_image_url,
                "star_count": starred_users.count(),
                "is_starred": is_starred,
                "starred_by_names": starred_by_names,
            }
        })

    return JsonResponse(data, safe=False)

def register(request):
    form = UserCreationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Account created successfully. Please log in to continue.")
        return redirect("main:login")

    context = {
        "first_name": "Nabila",
        "middle_name": "Oktavia",
        "last_name": "Ramadhani",
        "form": form,
    }
    return render(request, "register.html", context)

def login_user(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)
        response = redirect("main:show_main")
        response.set_cookie('last_login', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return response

    context = {
        "first_name": "Nabila",
        "middle_name": "Oktavia",
        "last_name": "Ramadhani",
        "form": form,
    }
    return render(request, "login.html", context)

def logout_user(request):
    logout(request)
    response = redirect("main:show_main")
    response.delete_cookie('last_login')
    return response

@login_required(login_url="/login/")
@require_POST
def toggle_star(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        if request.user in project.starred_by.all():
            project.starred_by.remove(request.user)
        else:
            project.starred_by.add(request.user)

    return redirect("main:show_project")

# AJAX ver

@require_POST
def create_project_ajax(request):
    if not request.user.is_superuser:
        return JsonResponse(
            {"message": "Only the portfolio owner can add projects."},
            status=403,
        )

    form = ProjectForm(request.POST)
    if form.is_valid():
        project = form.save()
        return JsonResponse(
            {"message": "New project successfully added!", "pk": str(project.id)},
            status=201,
        )

    return JsonResponse({"errors": form.errors.get_json_data()}, status=400)

@require_POST
def delete_project_ajax(request, project_id):
    if not request.user.is_superuser:
        return JsonResponse(
            {"message": "Only the portfolio owner can delete projects."},
            status=403,
        )

    project = get_object_or_404(Project, pk=project_id)
    project.delete()
    return JsonResponse({"message": "Project deleted successfully!"})

@require_POST
def edit_project_ajax(request, project_id):
    if not (request.user.is_superuser or is_editor(request.user)):
        return JsonResponse({"message": "You don't have permission to edit projects."}, status=403)

    project = get_object_or_404(Project, pk=project_id)
    form = ProjectForm(request.POST, instance=project)

    if form.is_valid():
        form.save()
        return JsonResponse({"message": "Project updated successfully!"})
    return JsonResponse({"errors": form.errors.get_json_data()}, status=400)