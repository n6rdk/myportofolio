from django.urls import path

from main.views import *

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("experience/", show_experience, name="show_experience"),
    path("experience/add/", create_experience, name="create_experience"),
    path("api/experience/", get_experience_json, name="get_experience_json"),
    path("experience/<uuid:experience_id>/delete/",delete_experience,name="delete_experience"),
    path("experience/<uuid:experience_id>/edit/", edit_experience, name="edit_experience"),
    path("skill/", show_skill, name="show_skill"),
    path("project/", show_project, name="show_project"),
    path("project/add/", create_project, name="create_project"),
    path("api/project/", get_project_json, name="get_project_json"),
    path("project/<uuid:project_id>/delete/",delete_project,name="delete_project"),
    path("project/<uuid:project_id>/edit/", edit_project, name="edit_project"),
    path("register/", register, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
    path("projects/<uuid:project_id>/star/", toggle_star, name="toggle_star"),
    path("projects/add-ajax/", create_project_ajax, name="create_project_ajax"),
    path(".well-known/appspecific/com.chrome.devtools.json", devtools_json_view)
]