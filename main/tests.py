import json
import uuid

from django.contrib.auth.models import Group, User
from django.test import Client, TestCase
from django.urls import reverse

from main.forms import ExperienceForm
from main.models import Education, Experience, Project, Skill


class BaseTestCase(TestCase):
    PASSWORDS = {
        "admin": "adminpass123",
        "editor": "editorpass123",
        "regular": "regularpass123",
    }

    def setUp(self):
        self.superuser = User.objects.create_superuser(
            username="admin", password=self.PASSWORDS["admin"]
        )

        self.editor_group, _ = Group.objects.get_or_create(name="Editor")
        self.editor_user = User.objects.create_user(
            username="editor", password=self.PASSWORDS["editor"]
        )
        self.editor_user.groups.add(self.editor_group)

        self.regular_user = User.objects.create_user(
            username="regular", password=self.PASSWORDS["regular"]
        )

        self.education = Education.objects.create(
            institution="Universitas Indonesia",
            major="Computer Science",
            started_at=2025,
        )
        self.experience = Experience.objects.create(
            title="OSN-K Informatics Participant",
            description="Competed in the district-level Informatics Olympiad.",
            category="competition",
            ended_at=2023,
        )
        self.skill = Skill.objects.create(
            field="Languages",
            icon="lucide:code",
            tech_stack=["Java", "Python", "C", "C++", "Bash", "SQL"],
        )
        self.project = Project.objects.create(
            title="My Portfolio Website",
            description="A personal portfolio built with Django.",
            tech_stack="Django, Python, HTML, CSS",
            project_url="https://github.com/example/myportofolio",
        )

    # ---------- helpers ----------

    def login_as(self, username=None):
        """Log in as the given user, or become anonymous when username is None."""
        self.client.logout()
        if username:
            self.client.login(username=username, password=self.PASSWORDS[username])

    def get_json(self, url, params=None):
        response = self.client.get(url, params or {})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response["content-type"], "application/json")
        return json.loads(response.content)

    def error_messages(self, response, field):
        errors = response.json()["errors"]
        return [error["message"] for error in errors[field]]

    def project_payload(self, **overrides):
        payload = {
            "title": "New Project",
            "description": "A new project.",
            "tech_stack": "Django",
            "project_url": "https://github.com/example/new",
            "project_image_url": "",
        }
        payload.update(overrides)
        return payload

    def experience_payload(self, **overrides):
        payload = {
            "title": "New Experience",
            "description": "desc",
            "category": "internship",
            "started_at": 2024,
        }
        payload.update(overrides)
        return payload

# PAGES
class PageTest(BaseTestCase):
    def assertFlag(self, response, name, expected):
        value = "true" if expected else "false"
        self.assertContains(response, f'const {name} = "{value}" === "true";')

    def test_main_url_is_accessible(self):
        response = self.client.get(reverse("main:show_main"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
        self.assertNotContains(response, self.experience.title)
        self.assertNotContains(response, self.skill.field)
        self.assertContains(response, self.education.major)
        self.assertContains(response, f'href="{reverse("main:show_experience")}"')
        self.assertContains(response, f'href="{reverse("main:show_skill")}"')

    def test_skill_url_is_accessible(self):
        response = self.client.get(reverse("main:show_skill"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "skill.html")
        self.assertNotContains(response, self.experience.title)
        self.assertNotContains(response, self.education.major)
        self.assertContains(response, self.skill.field)

    def test_nonexistent_page_returns_404(self):
        response = self.client.get("/halaman-yang-tidak-ada/")

        self.assertEqual(response.status_code, 404)

    def test_empty_education_section(self):
        Education.objects.all().delete()
        response = self.client.get(reverse("main:show_main"))

        self.assertContains(response, "No education records yet.")

    def test_empty_skill_page(self):
        Skill.objects.all().delete()
        response = self.client.get(reverse("main:show_skill"))

        self.assertContains(response, "No skills have been added yet.")

    def test_project_page_is_skeleton_without_data(self):
        response = self.client.get(reverse("main:show_project"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "project.html")
        for element_id in ("loading", "error", "empty", "grid"):
            self.assertContains(response, f'id="{element_id}"')
        # Data must come from the JSON endpoint, not from the first response
        self.assertNotContains(response, self.project.title)
        self.assertContains(response, f'href="{reverse("main:show_main")}"')

    def test_experience_page_is_skeleton_without_data(self):
        response = self.client.get(reverse("main:show_experience"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "experience.html")
        for element_id in ("loading", "error", "empty", "experience-list"):
            self.assertContains(response, f'id="{element_id}"')
        self.assertNotContains(response, self.experience.title)
        self.assertContains(response, f'href="{reverse("main:show_main")}"')

    def test_project_search_box_is_prefilled_from_query_string(self):
        response = self.client.get(reverse("main:show_project"), {"title": "Portfolio"})

        self.assertContains(response, 'value="Portfolio"')

    def test_experience_search_box_is_prefilled_from_query_string(self):
        response = self.client.get(reverse("main:show_experience"), {"category": "comp"})

        self.assertContains(response, 'value="comp"')

    # ----- role flags used by the JS to render buttons -----

    def test_project_page_role_flags_and_modal(self):
        cases = [
            # username, IS_SUPERUSER, CAN_EDIT
            (None, False, False),
            ("regular", False, False),
            ("editor", False, True),
            ("admin", True, True),
        ]
        for username, is_superuser, can_edit in cases:
            with self.subTest(user=username):
                self.login_as(username)
                response = self.client.get(reverse("main:show_project"))

                self.assertEqual(response.status_code, 200)
                self.assertFlag(response, "IS_SUPERUSER", is_superuser)
                self.assertFlag(response, "CAN_EDIT", can_edit)
                if can_edit:
                    self.assertContains(response, 'id="add-project-modal"')
                else:
                    self.assertNotContains(response, 'id="add-project-modal"')

    def test_experience_page_role_flags_and_modal(self):
        cases = [
            (None, False),
            ("regular", False),
            ("editor", False),
            ("admin", True),
        ]
        for username, is_superuser in cases:
            with self.subTest(user=username):
                self.login_as(username)
                response = self.client.get(reverse("main:show_experience"))

                self.assertEqual(response.status_code, 200)
                self.assertFlag(response, "IS_SUPERUSER", is_superuser)
                if is_superuser:
                    self.assertContains(response, 'id="add-experience-modal"')
                else:
                    self.assertNotContains(response, 'id="add-experience-modal"')

# MODELS
class ModelTest(BaseTestCase):
    def test_education_model(self):
        self.assertEqual(str(self.education), "Universitas Indonesia")
        self.assertEqual(self.education.major, "Computer Science")
        self.assertEqual(self.education.started_at, 2025)
        self.assertIsNone(self.education.ended_at)
        self.assertTrue(self.education.is_ongoing)

    def test_experience_model(self):
        self.assertEqual(str(self.experience), "OSN-K Informatics Participant")
        self.assertEqual(self.experience.category, "competition")
        self.assertEqual(self.experience.ended_at, 2023)
        self.assertTrue(self.experience.is_blank_start)

    def test_skill_model(self):
        self.assertEqual(str(self.skill), "Languages")
        self.assertEqual(self.skill.tech_stack, ["Java", "Python", "C", "C++", "Bash", "SQL"])

    def test_project_model(self):
        self.assertEqual(str(self.project), "My Portfolio Website")
        self.assertEqual(self.project.tech_stack, "Django, Python, HTML, CSS")
        self.assertEqual(self.project.project_url, "https://github.com/example/myportofolio")

# JSON ENDPOINTS (GET)
class ProjectJsonTest(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.url = reverse("main:get_project_json")

    def test_returns_pk_and_expected_fields(self):
        data = self.get_json(self.url)

        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["pk"], str(self.project.id))
        for key in (
            "title", "description", "tech_stack", "project_url",
            "project_image_url", "star_count", "is_starred", "starred_by_names",
        ):
            self.assertIn(key, data[0]["fields"])
        self.assertEqual(data[0]["fields"]["title"], self.project.title)

    def test_is_public_for_anonymous_visitors(self):
        self.login_as(None)
        data = self.get_json(self.url)

        self.assertEqual(len(data), 1)
        self.assertFalse(data[0]["fields"]["is_starred"])

    def test_search_by_title_is_case_insensitive(self):
        Project.objects.create(
            title="Unrelated App", description="Other.", tech_stack="Flask"
        )

        data = self.get_json(self.url, {"title": "portfolio"})

        self.assertEqual([p["fields"]["title"] for p in data], [self.project.title])

    def test_search_without_match_returns_empty_list(self):
        self.assertEqual(self.get_json(self.url, {"title": "nonexistent"}), [])

    def test_empty_database_returns_empty_list(self):
        Project.objects.all().delete()

        self.assertEqual(self.get_json(self.url), [])

    def test_star_information(self):
        self.project.starred_by.add(self.regular_user, self.editor_user)

        # anonymous: count is visible, personal status is not
        fields = self.get_json(self.url)[0]["fields"]
        self.assertEqual(fields["star_count"], 2)
        self.assertFalse(fields["is_starred"])
        self.assertCountEqual(fields["starred_by_names"].split(", "), ["regular", "editor"])

        # a user who starred it
        self.login_as("regular")
        self.assertTrue(self.get_json(self.url)[0]["fields"]["is_starred"])

        # a user who did not
        self.login_as("admin")
        self.assertFalse(self.get_json(self.url)[0]["fields"]["is_starred"])


class ExperienceJsonTest(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.url = reverse("main:get_experience_json")

    def by_title(self, data, title):
        return next(item for item in data if item["fields"]["title"] == title)

    def test_returns_pk_and_display_fields(self):
        data = self.get_json(self.url)

        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["pk"], str(self.experience.id))
        self.assertEqual(data[0]["fields"]["category_display"], "Competition")
        self.assertEqual(data[0]["fields"]["time_display"], "2023")

    def test_time_display_formats(self):
        Experience.objects.create(
            title="Both", description="d", category="research",
            started_at=2022, ended_at=2024,
        )
        Experience.objects.create(
            title="Ongoing", description="d", category="volunteer", started_at=2022,
        )

        data = self.get_json(self.url)

        self.assertEqual(self.by_title(data, "Both")["fields"]["time_display"], "2022 - 2024")
        self.assertEqual(self.by_title(data, "Ongoing")["fields"]["time_display"], "2022 - Present")

    def test_search_by_category_label_is_case_insensitive(self):
        Experience.objects.create(
            title="Lab", description="d", category="research", started_at=2022,
        )

        for query in ("comp", "COMP"):
            with self.subTest(query=query):
                data = self.get_json(self.url, {"category": query})
                self.assertEqual([e["fields"]["title"] for e in data], [self.experience.title])

        data = self.get_json(self.url, {"category": "research"})
        self.assertEqual([e["fields"]["title"] for e in data], ["Lab"])

    def test_search_without_match_returns_empty_list(self):
        self.assertEqual(self.get_json(self.url, {"category": "zzz"}), [])

    def test_empty_database_returns_empty_list(self):
        Experience.objects.all().delete()

        self.assertEqual(self.get_json(self.url), [])

# PROJECT AJAX (create / edit / delete)
class ProjectAjaxTest(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.create_url = reverse("main:create_project_ajax")
        self.edit_url = reverse("main:edit_project_ajax", args=[self.project.id])
        self.delete_url = reverse("main:delete_project_ajax", args=[self.project.id])

    # ----- create -----

    def test_create_forbidden_for_everyone_but_superuser(self):
        for username in (None, "regular", "editor"):
            with self.subTest(user=username):
                self.login_as(username)
                response = self.client.post(self.create_url, self.project_payload())

                self.assertEqual(response.status_code, 403)
                self.assertIn("message", response.json())
        self.assertEqual(Project.objects.count(), 1)

    def test_create_succeeds_for_superuser_with_201(self):
        self.login_as("admin")
        response = self.client.post(self.create_url, self.project_payload())

        self.assertEqual(response.status_code, 201)
        data = response.json()
        self.assertIn("message", data)
        self.assertTrue(Project.objects.filter(pk=data["pk"], title="New Project").exists())
        self.assertEqual(Project.objects.count(), 2)

    def test_create_invalid_data_returns_400_with_field_errors(self):
        self.login_as("admin")
        response = self.client.post(self.create_url, self.project_payload(title=""))

        self.assertEqual(response.status_code, 400)
        self.assertIn("title", response.json()["errors"])
        self.assertEqual(Project.objects.count(), 1)

    def test_create_rejects_invalid_url(self):
        self.login_as("admin")
        response = self.client.post(
            self.create_url, self.project_payload(project_url="javascript:alert(1)")
        )

        self.assertEqual(response.status_code, 400)
        self.assertIn("project_url", response.json()["errors"])

    def test_create_strips_html_tags(self):
        self.login_as("admin")
        response = self.client.post(
            self.create_url,
            self.project_payload(
                title="<b>Hello</b> World",
                description="<script>x</script>desc",
                tech_stack="<i>Django</i>",
            ),
        )

        self.assertEqual(response.status_code, 201)
        project = Project.objects.get(pk=response.json()["pk"])
        self.assertEqual(project.title, "Hello World")
        self.assertEqual(project.description, "xdesc")
        self.assertEqual(project.tech_stack, "Django")

    def test_create_rejects_title_that_is_only_html_tags(self):
        self.login_as("admin")
        response = self.client.post(self.create_url, self.project_payload(title="<b></b>"))

        self.assertEqual(response.status_code, 400)
        self.assertIn("title", response.json()["errors"])

    def test_create_rejects_get(self):
        self.login_as("admin")

        self.assertEqual(self.client.get(self.create_url).status_code, 405)

    # ----- edit -----

    def test_edit_allowed_for_editor_and_superuser(self):
        for username in ("editor", "admin"):
            with self.subTest(user=username):
                self.login_as(username)
                title = f"Updated by {username}"
                response = self.client.post(self.edit_url, self.project_payload(title=title))

                self.assertEqual(response.status_code, 200)
                self.project.refresh_from_db()
                self.assertEqual(self.project.title, title)
        self.assertEqual(Project.objects.count(), 1)

    def test_edit_forbidden_for_anonymous_and_regular_user(self):
        for username in (None, "regular"):
            with self.subTest(user=username):
                self.login_as(username)
                response = self.client.post(self.edit_url, self.project_payload(title="Hacked"))

                self.assertEqual(response.status_code, 403)
                self.project.refresh_from_db()
                self.assertEqual(self.project.title, "My Portfolio Website")

    def test_edit_invalid_data_returns_400_and_keeps_old_values(self):
        self.login_as("editor")
        response = self.client.post(self.edit_url, self.project_payload(title=""))

        self.assertEqual(response.status_code, 400)
        self.assertIn("title", response.json()["errors"])
        self.project.refresh_from_db()
        self.assertEqual(self.project.title, "My Portfolio Website")

    def test_edit_unknown_project_returns_404(self):
        self.login_as("admin")
        url = reverse("main:edit_project_ajax", args=[uuid.uuid4()])

        self.assertEqual(self.client.post(url, self.project_payload()).status_code, 404)

    def test_edit_rejects_get(self):
        self.login_as("admin")

        self.assertEqual(self.client.get(self.edit_url).status_code, 405)

    # ----- delete -----

    def test_delete_forbidden_for_everyone_but_superuser(self):
        for username in (None, "regular", "editor"):
            with self.subTest(user=username):
                self.login_as(username)
                response = self.client.post(self.delete_url)

                self.assertEqual(response.status_code, 403)
                self.assertTrue(Project.objects.filter(pk=self.project.id).exists())

    def test_delete_succeeds_for_superuser(self):
        self.login_as("admin")
        response = self.client.post(self.delete_url)

        self.assertEqual(response.status_code, 200)
        self.assertIn("message", response.json())
        self.assertFalse(Project.objects.filter(pk=self.project.id).exists())

    def test_delete_unknown_project_returns_404(self):
        self.login_as("admin")
        url = reverse("main:delete_project_ajax", args=[uuid.uuid4()])

        self.assertEqual(self.client.post(url).status_code, 404)

    def test_delete_rejects_get_and_keeps_data(self):
        self.login_as("admin")
        response = self.client.get(self.delete_url)

        self.assertEqual(response.status_code, 405)
        self.assertTrue(Project.objects.filter(pk=self.project.id).exists())

# EXPERIENCE AJAX (create / edit / delete)
class ExperienceAjaxTest(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.create_url = reverse("main:create_experience_ajax")
        self.edit_url = reverse("main:edit_experience_ajax", args=[self.experience.id])
        self.delete_url = reverse("main:delete_experience_ajax", args=[self.experience.id])

    # ----- create -----

    def test_create_forbidden_for_everyone_but_superuser(self):
        for username in (None, "regular", "editor"):
            with self.subTest(user=username):
                self.login_as(username)
                response = self.client.post(self.create_url, self.experience_payload())

                self.assertEqual(response.status_code, 403)
                self.assertIn("message", response.json())
        self.assertEqual(Experience.objects.count(), 1)

    def test_create_succeeds_for_superuser_with_201(self):
        self.login_as("admin")
        response = self.client.post(self.create_url, self.experience_payload())

        self.assertEqual(response.status_code, 201)
        data = response.json()
        self.assertTrue(
            Experience.objects.filter(pk=data["pk"], title="New Experience").exists()
        )
        self.assertEqual(Experience.objects.count(), 2)

    def test_create_requires_title(self):
        self.login_as("admin")
        response = self.client.post(self.create_url, self.experience_payload(title=""))

        self.assertEqual(response.status_code, 400)
        self.assertIn("title", response.json()["errors"])

    def test_create_requires_start_or_end_year(self):
        self.login_as("admin")
        payload = self.experience_payload()
        del payload["started_at"]
        response = self.client.post(self.create_url, payload)

        self.assertEqual(response.status_code, 400)
        self.assertIn(
            "Fill in at least a start or an end date.",
            self.error_messages(response, "__all__"),
        )

    def test_create_rejects_end_before_start(self):
        self.login_as("admin")
        response = self.client.post(
            self.create_url, self.experience_payload(started_at=2024, ended_at=2020)
        )

        self.assertEqual(response.status_code, 400)
        self.assertIn("ended_at", response.json()["errors"])
        self.assertEqual(Experience.objects.count(), 1)

    def test_create_rejects_invalid_category(self):
        self.login_as("admin")
        response = self.client.post(self.create_url, self.experience_payload(category="astronaut"))

        self.assertEqual(response.status_code, 400)
        self.assertIn("category", response.json()["errors"])

    def test_create_strips_html_tags(self):
        # Needs clean_title / clean_description with strip_tags in ExperienceForm
        self.login_as("admin")
        response = self.client.post(
            self.create_url,
            self.experience_payload(title="<b>Bold</b> Title", description="<script>x</script>desc"),
        )

        self.assertEqual(response.status_code, 201)
        experience = Experience.objects.get(pk=response.json()["pk"])
        self.assertEqual(experience.title, "Bold Title")
        self.assertEqual(experience.description, "xdesc")

    def test_create_rejects_title_that_is_only_html_tags(self):
        self.login_as("admin")
        response = self.client.post(self.create_url, self.experience_payload(title="<b></b>"))

        self.assertEqual(response.status_code, 400)
        self.assertIn("title", response.json()["errors"])

    def test_create_rejects_get(self):
        self.login_as("admin")

        self.assertEqual(self.client.get(self.create_url).status_code, 405)

    # ----- edit -----

    def test_edit_succeeds_for_superuser(self):
        self.login_as("admin")
        response = self.client.post(self.edit_url, self.experience_payload(title="Updated"))

        self.assertEqual(response.status_code, 200)
        self.experience.refresh_from_db()
        self.assertEqual(self.experience.title, "Updated")
        self.assertEqual(Experience.objects.count(), 1)

    def test_edit_forbidden_for_everyone_but_superuser(self):
        for username in (None, "regular", "editor"):
            with self.subTest(user=username):
                self.login_as(username)
                response = self.client.post(self.edit_url, self.experience_payload(title="Hacked"))

                self.assertEqual(response.status_code, 403)
                self.experience.refresh_from_db()
                self.assertEqual(self.experience.title, "OSN-K Informatics Participant")

    def test_edit_invalid_data_returns_400_and_keeps_old_values(self):
        self.login_as("admin")
        response = self.client.post(
            self.edit_url, self.experience_payload(started_at=2024, ended_at=2020)
        )

        self.assertEqual(response.status_code, 400)
        self.assertIn("ended_at", response.json()["errors"])
        self.experience.refresh_from_db()
        self.assertEqual(self.experience.title, "OSN-K Informatics Participant")

    def test_edit_unknown_experience_returns_404(self):
        self.login_as("admin")
        url = reverse("main:edit_experience_ajax", args=[uuid.uuid4()])

        self.assertEqual(self.client.post(url, self.experience_payload()).status_code, 404)

    def test_edit_rejects_get(self):
        self.login_as("admin")

        self.assertEqual(self.client.get(self.edit_url).status_code, 405)

    # ----- delete -----

    def test_delete_forbidden_for_everyone_but_superuser(self):
        for username in (None, "regular", "editor"):
            with self.subTest(user=username):
                self.login_as(username)
                response = self.client.post(self.delete_url)

                self.assertEqual(response.status_code, 403)
                self.assertTrue(Experience.objects.filter(pk=self.experience.id).exists())

    def test_delete_succeeds_for_superuser(self):
        self.login_as("admin")
        response = self.client.post(self.delete_url)

        self.assertEqual(response.status_code, 200)
        self.assertFalse(Experience.objects.filter(pk=self.experience.id).exists())

    def test_delete_unknown_experience_returns_404(self):
        self.login_as("admin")
        url = reverse("main:delete_experience_ajax", args=[uuid.uuid4()])

        self.assertEqual(self.client.post(url).status_code, 404)

    def test_delete_rejects_get_and_keeps_data(self):
        self.login_as("admin")
        response = self.client.get(self.delete_url)

        self.assertEqual(response.status_code, 405)
        self.assertTrue(Experience.objects.filter(pk=self.experience.id).exists())

# CSRF
class CsrfTest(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.create_url = reverse("main:create_project_ajax")
        self.client = Client(enforce_csrf_checks=True)  # the default client skips CSRF
        self.client.login(username="admin", password=self.PASSWORDS["admin"])

    def test_post_without_csrf_token_is_rejected(self):
        response = self.client.post(self.create_url, self.project_payload())

        self.assertEqual(response.status_code, 403)
        self.assertEqual(Project.objects.count(), 1)

    def test_post_with_x_csrftoken_header_is_accepted(self):
        self.client.get(reverse("main:show_project"))
        token = self.client.cookies["csrftoken"].value

        response = self.client.post(
            self.create_url, self.project_payload(), HTTP_X_CSRFTOKEN=token
        )

        self.assertEqual(response.status_code, 201)
        self.assertEqual(Project.objects.count(), 2)

    def test_post_with_wrong_csrf_token_is_rejected(self):
        self.client.get(reverse("main:show_project"))

        response = self.client.post(
            self.create_url, self.project_payload(), HTTP_X_CSRFTOKEN="wrong-token"
        )

        self.assertEqual(response.status_code, 403)
        self.assertEqual(Project.objects.count(), 1)

# STAR TOGGLE
class StarToggleTest(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.url = reverse("main:toggle_star", args=[self.project.id])

    def test_anonymous_user_is_redirected_to_login(self):
        response = self.client.post(self.url)

        self.assertRedirects(
            response, f"/login/?next={self.url}", fetch_redirect_response=False
        )
        self.assertEqual(self.project.starred_by.count(), 0)

    def test_logged_in_user_can_star_and_unstar(self):
        self.login_as("regular")

        response = self.client.post(self.url)
        self.assertRedirects(response, reverse("main:show_project"))
        self.assertIn(self.regular_user, self.project.starred_by.all())

        self.client.post(self.url)
        self.assertNotIn(self.regular_user, self.project.starred_by.all())

    def test_get_is_rejected(self):
        self.login_as("regular")

        self.assertEqual(self.client.get(self.url).status_code, 405)
        self.assertEqual(self.project.starred_by.count(), 0)

    def test_unknown_project_returns_404(self):
        self.login_as("regular")
        url = reverse("main:toggle_star", args=[uuid.uuid4()])

        self.assertEqual(self.client.post(url).status_code, 404)

# FORM VALIDATION
class FormTest(BaseTestCase):
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