from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import TaskForm
from task.models import UserTask
from django.contrib.auth.models import User


def TaskView(request):
    if request.user.is_authenticated:
        # queryset = UserTask.objects.all()
        task = UserTask.objects.filter(user=request.user)
        form = TaskForm()
        context = {
            'form': form, 'task': task, 'object_list': task,
        }
        return render(request, 'index.html', context)
    else:
        return redirect('login')


def add(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            text = form.cleaned_data['task']
            form = TaskForm()

    else:
        form = TaskForm()

    return redirect('task')


def delete(request, id):
    form = UserTask.objects.get(id=id)
    form.delete()

    return redirect('task')
