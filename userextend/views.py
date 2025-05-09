from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import CreateView, DetailView, UpdateView
import random
from userextend.forms import UserForm


# Create your views here.

class UserCreateView(CreateView):
    template_name = 'userextend/create_user.html'
    model = User
    form_class = UserForm
    success_url = '/login/'

    def form_valid(self, form):
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.first_name = new_user.first_name.lower().title()
            new_user.last_name = new_user.last_name.lower().title()

            new_user.username = f"{new_user.first_name[0].lower()}{new_user.last_name.replace(" ", "_").lower()}_{random.randint(100000, 999999)}"
            new_user.save()
        return super(UserCreateView, self).form_valid(form)


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'userextend/view_profile.html'

class UserEditView(LoginRequiredMixin, UpdateView):
    template_name = 'userextend/edit_profile.html'
    model = User
    form_class = UserForm
    success_url = ''