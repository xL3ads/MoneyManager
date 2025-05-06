import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, CreateView

from categories.models import UserCategory
from transactions.forms import TransactionForm
from transactions.models import UserTransactions


# Create your views here.

class TransactionCreateView(LoginRequiredMixin, CreateView):
    template_name = 'transactions/add_transaction.html'
    model = UserTransactions
    form_class = TransactionForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['user'] = self.request.user
        data['now'] = datetime.datetime.now()

        return data

    def form_valid(self, form):
        form.instance.user = self.request.user  # Setează utilizatorul curent
        return super().form_valid(form)

class TransactionListView(LoginRequiredMixin, ListView):
    template_name = 'transactions/list_of_transactions.html'
    model = UserTransactions
    context_object_name = 'all_transactions'

    def get_queryset(self):
        # Filtrare tranzacții după utilizatorul curent
        return UserTransactions.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['categories'] = UserCategory.objects.all()
        return data

