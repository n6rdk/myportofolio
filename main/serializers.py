from django.utils.html import strip_tags
from rest_framework import serializers

from main.models import *


class ProjectSerializer(serializers.ModelSerializer):
    star_count = serializers.SerializerMethodField()
    is_starred = serializers.SerializerMethodField()
    starred_by_names = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = [
            "id", "title", "description", "tech_stack",
            "project_url", "project_image_url",
            "star_count", "is_starred", "starred_by_names",
        ]
        read_only_fields = ["id"]

    def validate_title(self, value):
        value = strip_tags(value).strip()
        if not value:
            raise serializers.ValidationError("Title cannot be empty.")
        return value

    def validate_description(self, value):
        return strip_tags(value)

    def validate_tech_stack(self, value):
        return strip_tags(value)

    def get_star_count(self, obj):
        return obj.starred_by.count()

    def get_is_starred(self, obj):
        request = self.context.get("request")
        if request is None or not request.user.is_authenticated:
            return False
        return request.user in obj.starred_by.all()

    def get_starred_by_names(self, obj):
        return ", ".join(user.username for user in obj.starred_by.all())
    
class ExperienceSerializer(serializers.ModelSerializer):
    category_display = serializers.CharField(source="get_category_display", read_only=True)
    class Meta:
        model = Experience
        fields = [
            "id", "title", "description", "category", "category_display",
            "thumbnail", "started_at", "ended_at"
        ]
        read_only_fields = ["id"]
        
    def validate_title(self, value):
        value = strip_tags(value).strip()
        if not value:
            raise serializers.ValidationError("Title cannot be empty.")
        return value
    
    def validate_description(self, value):
        return strip_tags(value)
    
    def validate_category(self, value):
        value = strip_tags(value).strip()
        if not value:
            raise serializers.ValidationError("Category cannot be empty.")
        return value
    
    def validate(self, attrs):
        started_at = attrs.get("started_at", getattr(self.instance, "started_at", None))
        ended_at = attrs.get("ended_at", getattr(self.instance, "ended_at", None))

        if started_at is None and ended_at is None:
            raise serializers.ValidationError("At least one of started_at or ended_at is required.")

        return attrs
    
class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = [
            "id", "field", "icon", "tech_stack"
        ]
        read_only_fields = ["id"]
        
    def validate_field(self, value):
        value = strip_tags(value).strip()
        if not value:
            raise serializers.ValidationError("Field cannot be empty.")
        return value
    
    def validate_icon(self, value):
        return strip_tags(value).strip()
  
    def validate_tech_stack(self, value):
        if not isinstance(value, list):
            raise serializers.ValidationError("Tech stack must be a list of strings.")
        if not value:
            raise serializers.ValidationError("Tech stack cannot be empty.")

        cleaned_tech_stack = []
        for tech in value:
            if not isinstance(tech, str):
                raise serializers.ValidationError("Each tech stack item must be a string.")
            tech = strip_tags(tech).strip()
            if not tech:
                raise serializers.ValidationError("Tech stack items cannot be empty.")
            cleaned_tech_stack.append(tech)

        return cleaned_tech_stack
    
class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = [
            "id", "institution", "major", 
            "started_at", "ended_at"
        ]
        read_only_fields = ["id"]
        
    def validate_institution(self, value):
        value = strip_tags(value).strip()
        if not value:
            raise serializers.ValidationError("Institution cannot be empty.")
        return value
        
    def validate_major(self, value):
        value = strip_tags(value).strip()
        if not value:
            raise serializers.ValidationError("Major cannot be empty.")
        return value
