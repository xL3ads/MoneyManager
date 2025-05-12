from transactions.models import UserTransactions

def transactions_context(request):

    incomes = UserTransactions.objects.filter(user= request.user, category__is_income= True) # Imi filtreaza doar acele tranzactii care au category.is_income = True
    total_income = sum(income.amount for income in incomes) # Fac suma tuturor transactiilor de tip "income"

    expenses = UserTransactions.objects.filter(user= request.user, category__is_income= False) # Imi filtreaza doar acele tranzactii care au category.is_income = False
    total_expense = sum(expense.amount for expense in expenses) # Fac suma tuturor tranzactiilor de tip "expenses"

    total_money = total_income - total_expense

    first_name = request.user.first_name
    last_name = request.user.last_name
    fullname = f"{first_name} {last_name}"

    context = {
        'm': total_money,
        'full_name': fullname,
    }


    return context