from django.shortcuts import render, redirect
from django.views import View
from todo_app.models import Task, Comment
from todo_app.forms import TaskForm, CommentForm
# Create your views here.

class HomeView(View):
    '''
    Homeview functions as the site's homepage, listing out all Tasks objects
    in the database and linking out to each one's detail view.
    '''
    def get(self, request):
        ''' The content required to render the homepage'''
        task_form = TaskForm()
        tasks = Task.objects.all()

        html_data = {
            'task_list': tasks,
            'form': task_form,
        }

        return render(
            request=request,
            template_name='index.html',
            context= html_data
        )

    def post(self,request):
        '''
        This method saves new Tasks to the database before redirecting 
        to the "get" method of the hoomepage.
        '''
        task_form = TaskForm(request.POST)
        task_form.save()

        return redirect('home')

class TaskDetailView(View):
    '''
    TaskDetailView provides the ability to update and delete individual 
    Task objects from the database.
    '''
    def get(self, request, task_id):
        task = Task.objects.get(id=task_id)
        task_form = TaskForm(instance=task)


        comments = Comment.objects.filter(task=task)
        comment_form = CommentForm(task_object=task)

        html_data = {
            'task_object': task,
            'form': task_form,
            'comment_list':comments,
            'comment_form':comment_form
        }

        return render(
            request=request,
            template_name='detail.html',
            context= html_data
        )

    def post(self, request, task_id):
        '''
        This method either updates or deletes existing Task objects in the
        database(depending on user choice) before redirecting to the "get" method of the homepage.
        '''
        task = Task.objects.get(id=task_id)

        if 'update' in request.POST:
            task_form = TaskForm(request.POST, instance=task)
            task_form.save()
        elif 'delete' in request.POST:
            task.delete()
        elif 'add' in request.POST:
            comment_form = CommentForm(request.POST, task_object=task)
            comment_form.save()
            return redirect('task_detail', task_id)

        return redirect('home')
