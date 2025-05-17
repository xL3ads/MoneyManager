from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render

from categories.models import UserCategory
from transactions.models import UserTransactions


# Create your views here.
@login_required
def dashboard_view(request):

    get_month = request.GET.get('month')
    get_year = request.GET.get('year')

    if get_month and get_year:
        context={'all_data': UserTransactions.objects.filter(month=int(get_month), year=int(get_year), user_id=request.user.id)}
    else:
        context={}

    return render(request, 'dashboard/dashboard.html', context)






