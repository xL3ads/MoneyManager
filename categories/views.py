import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import CreateView, ListView

from categories.forms import CategoryFrom
from categories.models import UserCategory


# Create your views here.

class CategoryCreateView(LoginRequiredMixin, CreateView):
    template_name = 'categories/add_category.html'
    model = UserCategory
    form_class = CategoryFrom
    success_url = '/'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['user'] = self.request.user
        data['now'] = datetime.datetime.now()

        return data

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
#
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

