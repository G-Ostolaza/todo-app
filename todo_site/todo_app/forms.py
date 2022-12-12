from django.forms import ModelForm
from todo_app.models import Task, Comment

# creating form model class
class TaskForm(ModelForm):
    '''Pull the description column from the Task model into a form'''
    class Meta:
        model = Task
        fields =['description']

class CommentForm(ModelForm):
    '''Pull the description column from the Task model into a form'''
    class Meta:
        model = Comment
        fields =['body']

    # The form will get created with a task. We need to pull that task out
    # and keep track of it
    def __init__(self, *args, **kwargs):
        task =kwargs.pop('task_object')
        super().__init__(*args, **kwargs)

        # self.instance is the comment that we are creating  with this form
        self.instance.task =task

