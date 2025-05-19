from transactions.models import UserTransactions
from categories.models import UserCategory
from django.contrib.auth.models import User
from datetime import date, datetime

# Functie built in django
from django.db.models import Sum

def transactions_context(request):

    context = {}

    if request.user.is_authenticated:
        incomes = UserTransactions.objects.filter(user=request.user, category__is_income=True, date__year=datetime.now().year)
        total_income = sum(income.amount for income in incomes)

        expenses = UserTransactions.objects.filter(user=request.user, category__is_income=False, date__year=datetime.now().year)
        total_expense = sum(expense.amount for expense in expenses)

        total_money = total_income - total_expense

        first_name = request.user.first_name
        last_name = request.user.last_name
        fullname = f"{first_name} {last_name}"

        context = {
            'total_money': total_money,
            'full_name': fullname,
            'year': datetime.now().year,
        }

    return context
