from django.urls import path

from transactions import views
from transactions.views import TransactionCreateView

urlpatterns = [
    path('add_transaction/',views.TransactionCreateView.as_view(), name='add-transaction'),
    path('list_of_transactions/',views.TransactionListView.as_view(), name='list-of-transactions'),
]