from django.urls import path

from main.views import *

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("register/", register, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
    
    path("experiences/", show_experience, name="show_experience"),
    path("experiences/add/", create_experience, name="create_experience"),
    path("api/experiences/", get_experience_json, name="get_experience_json"),
    path("experiences/<uuid:experience_id>/delete/",delete_experience,name="delete_experience"),
    path("experiences/<uuid:experience_id>/edit/", edit_experience, name="edit_experience"),
    path("experiences/add-ajax/", create_experience_ajax, name="create_experience_ajax"),
    path("experiences/<uuid:experience_id>/delete/ajax/", delete_experience_ajax, name="delete_experience_ajax"),
    path("experiences/<uuid:experience_id>/edit/ajax/", edit_experience_ajax, name="edit_experience_ajax"),
    
    path("skills/", show_skill, name="show_skill"),
    
    path("projects/", show_project, name="show_project"),
    path("projects/add/", create_project, name="create_project"),
    path("api/projects/", get_project_json, name="get_project_json"),
    path("projects/<uuid:project_id>/delete/",delete_project,name="delete_project"),
    path("projects/<uuid:project_id>/edit/", edit_project, name="edit_project"),
    path("projects/<uuid:project_id>/star/", toggle_star, name="toggle_star"),
    path("projects/add-ajax/", create_project_ajax, name="create_project_ajax"),
    path("projects/<uuid:project_id>/delete/ajax/", delete_project_ajax, name="delete_project_ajax"),
    path("projects/<uuid:project_id>/edit/ajax/", edit_project_ajax, name="edit_project_ajax"),
]