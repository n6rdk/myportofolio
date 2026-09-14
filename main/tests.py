from django.test import TestCase
from django.urls import reverse

from main.models import *


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