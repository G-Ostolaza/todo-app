from django.forms import ModelForm
from todo_app.models import Task

# creating form model class
class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields =['description']