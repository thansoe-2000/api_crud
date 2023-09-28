from rest_framework import serializers
from .models import *

class TaskSerializer(serializers.ModelSerializer):
     class Meta:
          model = Task
          fields = "__all__"

class LanguageSerializer(serializers.ModelSerializer):
     class Meta:
          model = Language
          fields = "__all__"