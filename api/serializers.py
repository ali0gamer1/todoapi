from rest_framework import serializers
from todo.models import *


class TodoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ["title", "description", "completed","user"]
    
