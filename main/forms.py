from django.core.exceptions import ValidationError
from django.forms import ModelForm, NumberInput, TextInput, Textarea, URLInput

from main.models import Experience, Project


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = [
            "title",
            "description",
            "tech_stack",
            "project_url",
            "project_image_url",
        ]

        labels = {
            "title": "Project Name",
            "description": "Description",
            "tech_stack": "Tech Stack",
            "project_url": "Project URL",
            "project_image_url": "Project Thumbnail URL",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Portfolio Website",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Describe your project",
                    "rows": 3,
                }
            ),
            "tech_stack": TextInput(
                attrs={
                    "placeholder": "Django, Python, HTML, CSS",
                }
            ),
            "project_url": URLInput(
                attrs={
                    "placeholder": "https://github.com/kakBurhan/burhanquestv4",
                }
            ),
            "project_image_url": URLInput(
                attrs={
                    "placeholder": "https://drive.google.com/thumbnail?id=...&sz=w1000",
                }
            ),
        }


class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = [
            "title",
            "description",
            "category",
            "thumbnail",
            "started_at",
            "ended_at",
        ]

        labels = {
            "title": "Experience Name",
            "description": "Description",
            "category": "Select Category",
            "thumbnail": "Experience Thumbnail URL",
            "started_at": "Year Started",
            "ended_at": "Year Ended (leave empty if ongoing)",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Teaching Assistant",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Describe your experience",
                    "rows": 3,
                }
            ),
            "thumbnail": URLInput(
                attrs={
                    "placeholder": "https://drive.google.com/thumbnail?id=...&sz=w1000",
                }
            ),
            "started_at": NumberInput(
                attrs={
                    "placeholder": "2021"
                }
            ),
            "ended_at": NumberInput(
                attrs={
                    "placeholder": "2026"
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["category"].choices = [("", "Choose one")] + list(
            Experience.EXPERIENCE_CHOICES
        )

    def clean(self):
        cleaned = super().clean()
        start = cleaned.get("started_at")
        end = cleaned.get("ended_at")

        if not start and not end:
            raise ValidationError("Fill in at least a start or an end date.")
        if start and end and start > end:
            self.add_error("ended_at", "End date must be after the start date.")
        return cleaned