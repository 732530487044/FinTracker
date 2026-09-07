from django.shortcuts import render
from django.db.models import Sum
from expences.models import Expences
from income.models import Income
from datetime import date

def home_view(request):
    total_expenses = Expences.objects.filter(user=request.user).aggregate(Sum('amount')) or 0

    total_income = Income.objects.filter(user=request.user).aggregate(Sum('amount') ) or 0

    total_saving = int(total_income['amount__sum'])-int(total_expenses['amount__sum'])

    today=date.today()
    this_month_expences=Expences.objects.filter(user=request.user,date__year=today.year,date__month=today.month).aggregate(Sum('amount'))
    this_month_income=Income.objects.filter(user=request.user,date__year=today.year,date__month=today.month).aggregate(Sum('amount'))
    this_month_saving = int(this_month_income['amount__sum'])-int(this_month_expences['amount__sum'])

    context = {
        'total_expenses': total_expenses['amount__sum'],
        'total_income': total_income['amount__sum'],
        'balance': total_saving,
        'this_month_saving':this_month_saving,
    }
    return render(request, 'pages/home.html',context)
def aboutus_view(request):
    return render(request, 'pages/about.html')