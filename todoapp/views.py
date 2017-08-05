from django.shortcuts import render
from todoapp.models import ToDoElements
from todoapp.serializers import TodoSerializer
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView,
)

# Create your views here.
def todo(request):
    return render(request, 'todo.html', {})

class Todolist(ListAPIView):
    queryset = ToDoElements.objects.all()    
    serializer_class = TodoSerializer

    def get_queryset(self):        
        return ToDoElements.objects.filter(done=False)
        

class Todoadd(CreateAPIView):
    queryset = ToDoElements.objects.all()    
    serializer_class = TodoSerializer

class Todoupdate(UpdateAPIView):
    queryset = ToDoElements.objects.all()    
    serializer_class = TodoSerializer

class Tododelete(DestroyAPIView):
    queryset = ToDoElements.objects.all()    
    serializer_class = TodoSerializer
