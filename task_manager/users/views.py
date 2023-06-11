from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.views import View

from task_manager.users.forms import RegisterUserForm
from task_manager.users.models import User


class IndexView(View):

    def get(self, request, *args, **kwargs):
        users = User.objects.all()
        return render(request, 'users/index.html', context={
            'users': users,
        })


class CreateView(View):

    def get(self, request, *args, **kwargs):
        form = RegisterUserForm()
        return render(request, 'users/create.html', context={
            'form': form,
        })

    def post(self, request, *args, **kwargs):
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'You have singed up successfully.')
            return redirect('login')
        else:
            return render(request, 'users/create.html', {'form': form})


class UpdateView(View):
    def get(self, request, *args, **kwargs):
        user_id = kwargs.get('pk')

        if not request.user.is_authenticated:
            messages.error(request, 'Please Log in!')
            return redirect('login')

        elif user_id != request.user.id:
            messages.error(request, 'You have no rights to change user')
            return redirect('users_index')

        user = User.objects.get(id=user_id)
        form = RegisterUserForm(instance=user)
        return render(request, 'users/update.html', context={
            'form': form,
            'user_id': user_id,
        })

    def post(self, request, *args, **kwargs):
        user_id = kwargs.get('pk')

        if not request.user.is_authenticated:
            return redirect('login')

        if user_id != request.user.id:
            return redirect('users_index')

        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.pk = user_id
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'You have changed your profile')
            return redirect('users_index')
        else:
            return render(request, 'users/update.html', context={
                'form': form,
                'user_id': user_id
                })


class UserDeleteView(View):

    def get(self, request, *args, **kwargs):
        user_id = kwargs.get('pk')

        if not request.user.is_authenticated:
            messages.error(request, 'Please Log in!')
            return redirect('login')

        elif user_id != request.user.id:
            messages.error(request, 'You have no rights to delete users')
            return redirect('users_index')

        user = User.objects.get(id=user_id)
        return render(request, 'users/delete.html', context={
            'user_name': user.username,
            'user_id': user_id,
        })

    def post(self, request, *args, **kwargs):
        user_id = kwargs.get('pk')

        if not request.user.is_authenticated:
            return redirect('login')

        if user_id != request.user.id:
            return redirect('users_index')

        user = User.objects.get(id=user_id)
        if user:
            user.delete()
        return redirect('users_index')
