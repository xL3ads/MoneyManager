import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView, TemplateView

from categories.models import UserCategory
from transactions.forms import TransactionForm, TransactionUpdateForm
from transactions.models import UserTransactions


# Create your views here.

class TransactionCreateView(LoginRequiredMixin, CreateView):
    template_name = 'transactions/add_transaction.html'
    model = UserTransactions
    form_class = TransactionForm
    success_url = '/'

    # Trimit userul in formular ca sa imi foloseasca doar acele categorii pe care le a creat userul
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['user'] = self.request.user
        data['now'] = datetime.datetime.now()

        return data

    def form_valid(self, form):
        if form.is_valid():
            new_transaction = form.save(commit=False)
            new_transaction.user = self.request.user

            data = new_transaction.date # creez un obiect data care salveaza data din baza de date
            new_transaction.month = data.month # salvez luna din obiectul data
            new_transaction.year = data.year # salvez anul din obiectul data
        return super().form_valid(form)


class TransactionListView(LoginRequiredMixin, ListView):
    template_name = 'transactions/list_of_transactions.html'
    model = UserTransactions
    context_object_name = 'all_transactions'

    def get_queryset(self):
        # Filtrare tranzacții după utilizatorul curent
        transactions = UserTransactions.objects.filter(user=self.request.user)

        # primesc informatiile din formular
        filter_year = self.request.GET.get('year')
        filter_month = self.request.GET.get('month')


        # toate tranzactiile mele sunt filtrate in aceasta ordine An -> Luna
        if filter_year:
            transactions = transactions.filter(date__year=filter_year)

        if filter_month:
            transactions = transactions.filter(date__month=filter_month)

        return transactions


    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['categories'] = UserCategory.objects.all()
        return data

class TransactionUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'transactions/update_transaction.html'
    model = UserTransactions
    form_class = TransactionUpdateForm
    success_url = '/list_of_transactions/'

class TransactionDetailView(LoginRequiredMixin, DetailView):
    template_name = 'transactions/details_transaction.html'
    model = UserTransactions

class TransactionDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'transactions/delete_transaction.html'
    model = UserTransactions
    success_url = '/list_of_transactions/'



