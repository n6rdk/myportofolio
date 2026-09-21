import json
from unittest.mock import patch

from django.test import TestCase
from django.urls import reverse

from main import views
from main.forms import ExperienceForm
from main.models import *

TEST_SECRET_KEY = "testkey123"

use_test_secret_key = patch.object(
    views.settings, "PORTFOLIO_SECRET_KEY", TEST_SECRET_KEY
)


class MainTest(TestCase):
    def setUp(self):
        self.education = Education.objects.create(
                            institution="Universitas Indonesia",
                            major="Computer Science",
                            started_at="2025"
                        )
        
        self.experience = Experience.objects.create(
                            title="OSN-K Informatics Participant",
                            description="Competed in the district-level Informatics Olympiad.",
                            category="competition",
                            ended_at="2023",
                        )
        
        self.skill = Skill.objects.create(
                        field="Languages",
                        icon="lucide:code",
                        tech_stack=["Java", "Python", "C", "C++", "Bash", "SQL"]
                    )
        self.project = Project.objects.create(
                        title="My Portfolio Website",
                        description="A personal portfolio built with Django.",
                        tech_stack="Django, Python, HTML, CSS",
                        project_url="https://github.com/example/myportofolio",
                    )

    def test_main_url_is_accessible(self):
        response = self.client.get(reverse("main:show_main"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
        self.assertNotContains(response, self.experience.title)
        self.assertNotContains(response, self.skill.field)
        self.assertContains(response, self.education.major)
        self.assertContains(response, f'href="{reverse("main:show_experience")}"')
        self.assertContains(response, f'href="{reverse("main:show_skill")}"')
    
    def test_experience_url_is_accessible(self):
        response = self.client.get(reverse("main:show_experience"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "experience.html")
        self.assertNotContains(response, self.skill.field)
        self.assertNotContains(response, self.education.major)
        self.assertContains(response, self.experience.title)
        self.assertContains(response, f'href="{reverse("main:show_main")}"')
        self.assertContains(response, f'href="{reverse("main:show_skill")}"')
    
    def test_skill_url_is_accessible(self):
        response = self.client.get(reverse("main:show_skill"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "skill.html")
        self.assertNotContains(response, self.experience.title)
        self.assertNotContains(response, self.education.major)
        self.assertContains(response, self.skill.field)
        self.assertContains(response, f'href="{reverse("main:show_main")}"')
        self.assertContains(response, f'href="{reverse("main:show_experience")}"')

    def test_project_url_is_accessible(self):
        response = self.client.get(reverse("main:show_project"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "project.html")
        self.assertContains(response, self.project.title)
        self.assertContains(response, f'href="{reverse("main:show_main")}"')
        self.assertContains(response, f'href="{reverse("main:show_experience")}"')
        
    def test_nonexistent_page_returns_404(self):
        response = self.client.get("/halaman-yang-tidak-ada/")

        self.assertEqual(response.status_code, 404)

    def test_education_model(self):
        self.assertEqual(str(self.education), "Universitas Indonesia")
        self.assertEqual(self.education.major, "Computer Science")
        self.assertEqual(self.education.started_at, "2025")
        self.assertEqual(self.education.ended_at, None)

    def test_experience_model(self):
        self.assertEqual(str(self.experience), "OSN-K Informatics Participant")
        self.assertEqual(self.experience.description, "Competed in the district-level Informatics Olympiad.")
        self.assertEqual(self.experience.category, "competition")
        self.assertEqual(self.experience.ended_at, "2023")

    def test_skill_model(self):
        self.assertEqual(str(self.skill), "Languages")
        self.assertEqual(self.skill.tech_stack, ["Java", "Python", "C", "C++", "Bash", "SQL"])

    def test_project_model(self):
        self.assertEqual(str(self.project), "My Portfolio Website")
        self.assertEqual(self.project.tech_stack, "Django, Python, HTML, CSS")
        self.assertEqual(self.project.project_url, "https://github.com/example/myportofolio")
        
    def test_empty_education_section(self):
        Education.objects.all().delete()
        response = self.client.get(reverse("main:show_main"))

        self.assertContains(response, "No education records yet.")
        
    def test_empty_experience_page(self):
        Experience.objects.all().delete()
        response = self.client.get(reverse("main:show_experience"))

        self.assertContains(response, "No experiences have been added yet.")
        
    def test_empty_skill_page(self):
        Skill.objects.all().delete()
        response = self.client.get(reverse("main:show_skill"))

        self.assertContains(response, "No skills have been added yet.")
        
    def test_empty_project_page(self):
        Project.objects.all().delete()
        response = self.client.get(reverse("main:show_project"))

        self.assertContains(response, "No projects have been added yet.")
    
    def test_project_search_filters_by_title(self):
        Project.objects.create(
            title="Unrelated App",
            description="Something else entirely.",
            tech_stack="Flask",
        )

        response = self.client.get(reverse("main:show_project"), {"title": "Portfolio"})

        self.assertContains(response, self.project.title)
        self.assertNotContains(response, "Unrelated App")
    
    # ====== JSON ENDPOINTS ======
    
    def test_get_experience_json(self):
        response = self.client.get(reverse("main:get_experience_json"))
        data = json.loads(response.content)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response["content-type"], "application/json")
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["fields"]["title"], self.experience.title)

    def test_get_project_json(self):
        response = self.client.get(reverse("main:get_project_json"))
        data = json.loads(response.content)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response["content-type"], "application/json")
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["fields"]["title"], self.project.title)

    def test_get_project_json_with_title_query(self):
        response = self.client.get(reverse("main:get_project_json"), {"title": "nonexistent"})
        data = json.loads(response.content)

        self.assertEqual(len(data), 0)
        
    # ====== SECRET-KEY-PROTECTED ACTIONS ======

    @use_test_secret_key
    def test_create_experience_fails_with_wrong_secret_key(self):
        response = self.client.post(reverse("main:create_experience"), {
            "title": "New Experience",
            "description": "desc",
            "category": "internship",
            "started_at": 2024,
            "secret_key": "wrongkey",
        })

        self.assertEqual(Experience.objects.count(), 1)  # unchanged
        self.assertRedirects(response, reverse("main:create_experience"))

    @use_test_secret_key
    def test_create_experience_succeeds_with_correct_secret_key(self):
        response = self.client.post(reverse("main:create_experience"), {
            "title": "New Experience",
            "description": "desc",
            "category": "internship",
            "started_at": 2024,
            "secret_key": TEST_SECRET_KEY,
        })

        self.assertEqual(Experience.objects.count(), 2)
        self.assertRedirects(response, reverse("main:show_experience"))

    @use_test_secret_key
    def test_delete_experience_requires_correct_secret_key(self):
        url = reverse("main:delete_experience", args=[self.experience.id])

        self.client.post(url, {"secret_key": "wrongkey"})
        self.assertEqual(Experience.objects.count(), 1)

        self.client.post(url, {"secret_key": TEST_SECRET_KEY})
        self.assertEqual(Experience.objects.count(), 0)

    @use_test_secret_key
    def test_delete_project_requires_correct_secret_key(self):
        url = reverse("main:delete_project", args=[self.project.id])

        self.client.post(url, {"secret_key": "wrongkey"})
        self.assertEqual(Project.objects.count(), 1)

        self.client.post(url, {"secret_key": TEST_SECRET_KEY})
        self.assertEqual(Project.objects.count(), 0)

    @use_test_secret_key
    def test_edit_project_updates_data_with_correct_secret_key(self):
        url = reverse("main:edit_project", args=[self.project.id])

        response = self.client.post(url, {
            "title": "Updated Title",
            "description": self.project.description,
            "tech_stack": self.project.tech_stack,
            "project_url": self.project.project_url,
            "project_image_url": "",
            "secret_key": TEST_SECRET_KEY,
        })

        self.project.refresh_from_db()
        self.assertEqual(self.project.title, "Updated Title")
        self.assertRedirects(response, reverse("main:show_project"))

    # ====== FORM VALIDATION ======

    def test_experience_form_requires_start_or_end_date(self):
        form = ExperienceForm(data={
            "title": "No dates",
            "description": "desc",
            "category": "internship",
        })

        self.assertFalse(form.is_valid())
        self.assertIn("Fill in at least a start or an end date.", form.errors.get("__all__", []))

    def test_experience_form_rejects_end_before_start(self):
        form = ExperienceForm(data={
            "title": "Bad dates",
            "description": "desc",
            "category": "internship",
            "started_at": 2024,
            "ended_at": 2020,
        })

        self.assertFalse(form.is_valid())
        self.assertIn("End date must be after the start date.", form.errors.get("ended_at", []))

    def test_experience_form_valid_with_correct_dates(self):
        form = ExperienceForm(data={
            "title": "Valid Experience",
            "description": "desc",
            "category": "internship",
            "started_at": 2022,
            "ended_at": 2024,
        })

        self.assertTrue(form.is_valid())