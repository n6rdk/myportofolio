import uuid
from django.db import models

class Experience(models.Model):
    EXPERIENCE_CHOICES = [
        ('internship', 'Internship'),
        ('research', 'Research'),
        ('volunteer', 'Volunteer'),
        ('part-time', 'Part-Time'),
        ('full-time', 'Full-Time'),
        ('freelance', 'Freelance'),
        ('competition', 'Competition'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=EXPERIENCE_CHOICES, default='full-time')
    thumbnail = models.URLField(blank=True, null=True)
    started_at = models.PositiveIntegerField(blank=True, null=True)
    ended_at = models.PositiveIntegerField(blank=True, null=True)
    
    def __str__(self):
        return self.title
    
    @property
    def is_ongoing(self):
        return self.ended_at is None
    
    @property
    def is_blank_start(self):
        return self.started_at is None
    
class Skill(models.Model):
    field = models.CharField(max_length=128)
    icon = models.CharField(max_length=64, blank=True, default='lucide:code')
    tech_stack = models.JSONField(blank=True, default=list)
    
    def __str__(self):
            return self.field
        
class Education(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    institution = models.CharField(max_length=255)
    major = models.CharField(max_length=255)
    started_at = models.PositiveIntegerField(blank=True, null=True)
    ended_at = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return self.institution

    @property
    def is_ongoing(self):
        return self.ended_at is None