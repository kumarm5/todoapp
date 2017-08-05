from django.db import models

# Create your models here.
class ToDoElements(models.Model):
    todo_text = models.CharField(max_length=200, blank=True, null=True)
    done = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

