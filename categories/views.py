import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import CreateView, ListView, DeleteView

from categories.forms import CategoryForm
from categories.models import UserCategory


# Create your views here.

class CategoryCreateView(LoginRequiredMixin, CreateView):
    template_name = 'categories/add_category.html'
    model = UserCategory
    form_class = CategoryForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['user'] = self.request.user
        data['now'] = datetime.datetime.now()

        return data

    def form_valid(self, form):

        #stocam numele categoriei si deasemenea si userul
        get_name = form.cleaned_data['name']
        user=self.request.user

        category_filter_name = UserCategory.objects.filter(name=get_name, user=user)

        # daca se gaseste o categorie a utilizatorului cu acelasi nume, utilizatorul va primi eroare
        if category_filter_name:
            form.add_error('name',f'Category "{get_name}" already exists')
            return self.form_invalid(form)

        # pastram instanta userului
        form.instance.user = user
        return super().form_valid(form)

class CategoryListView(LoginRequiredMixin, ListView):
    template_name = 'categories/list_category.html'
    model = UserCategory
    context_object_name = 'all_categories'

    def get_queryset(self):
        # Filtrare categorii dupa utilizatorul curent
        return UserCategory.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['user'] = self.request.user
        return data

class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'categories/delete_category.html'
    model = UserCategory
    success_url = '/list_category/'