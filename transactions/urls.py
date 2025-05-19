from django.urls import path

from transactions import views
from transactions.views import (TransactionCreateView, TransactionDetailView, TransactionUpdateView,
                                TransactionDeleteView)

urlpatterns = [
    path('add_transaction/',views.TransactionCreateView.as_view(), name='add-transaction'),
    path('list_of_transactions/',views.TransactionListView.as_view(), name='list-of-transactions'),
    path('update_transaction/<int:pk>', views.TransactionUpdateView.as_view(), name='update-transaction'),
    path('details_transaction/<int:pk>', views.TransactionDetailView.as_view(), name='details-transaction'),
    path('delete_transaction/<int:pk>', views.TransactionDeleteView.as_view(), name='delete-transaction'),
]