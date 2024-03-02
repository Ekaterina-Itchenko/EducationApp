from rest_framework import serializers
from core.models import Lesson


class LessonInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ("name", "video_link")
