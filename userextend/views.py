from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import render
from django.views.generic import CreateView, DetailView, UpdateView
import random

from MoneyManager.settings import DEFAULT_FROM_EMAIL
from userextend.forms import UserForm


# Create your views here.

class UserCreateView(CreateView):
    template_name = 'userextend/create_user.html'
    model = User
    form_class = UserForm
    success_url = '/login/'


    def form_valid(self, form):
        all_users = User.objects.all()
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.first_name = new_user.first_name.lower().title()
            new_user.last_name = new_user.last_name.lower().title()

            new_user.username = f"{new_user.first_name[0].lower()}{new_user.last_name.replace(" ", "_").lower()}_{random.randint(100000, 999999)}"
            new_user.save()

            # Trimitem un mail
            subject = "Money Manager - Account Details"
            message = (f"Hello {new_user.first_name} {new_user.last_name},\n\n\n"
                       f"Your MoneyManager account has been created successfully.\n"
                       f"Below you have the details about your account.\n"
                       f"For the authentification you need this user: {new_user.username} \n\n\n"
                       f"Kinds regards,\n"
                       f"Money Manager Staff")

            send_mail(subject, message, DEFAULT_FROM_EMAIL, [new_user.email])
        return super(UserCreateView, self).form_valid(form)


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'userextend/view_profile.html'

class UserEditView(LoginRequiredMixin, UpdateView):
    template_name = 'userextend/edit_profile.html'
    model = User
    form_class = UserForm
    success_url = ''