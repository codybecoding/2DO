from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout


# Create your views here.
def add_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('task')
    else:
        form = UserCreationForm()

    context = {
        'form' : form,
    }

    return render(request, 'home.html', context)


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # login(request, form)
            user = form.get_user()
            login(request, user)
            return redirect('task')
    else:
        form = AuthenticationForm(data=request.POST)
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)

    return redirect('login')
