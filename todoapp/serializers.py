from rest_framework.serializers import ModelSerializer

from todoapp.models import ToDoElements

class TodoSerializer(ModelSerializer):
    class Meta:
        model = ToDoElements
        fields = ('id', 'todo_text', 'done', 'created_at', 'updated_at')
