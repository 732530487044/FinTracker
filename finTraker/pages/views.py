from django.shortcuts import render
from django.db.models import Sum
from django.db.models.functions import TruncMonth
from django.utils import timezone

from expences.models import Expences
from income.models import Income


def home_view(request):

    total_expenses = 0
    total_income = 0
    total_saving = 0

    this_month_saving = 0

    expences = Expences.objects.none()

    months = []
    monthly_expenses = []

    if request.user.is_authenticated:

        total_expenses = (
            Expences.objects.filter(user=request.user)
            .aggregate(Sum('amount'))
            .get('amount__sum') or 0
        )

        total_income = (
            Income.objects.filter(user=request.user)
            .aggregate(Sum('amount'))
            .get('amount__sum') or 0
        )

        total_saving = total_income - total_expenses

        today = timezone.localdate()

        this_month_expenses = (
            Expences.objects.filter(
                user=request.user,
                date__year=today.year,
                date__month=today.month
            )
            .aggregate(Sum('amount'))
            .get('amount__sum') or 0
        )

        this_month_income = (
            Income.objects.filter(
                user=request.user,
                date__year=today.year,
                date__month=today.month
            )
            .aggregate(Sum('amount'))
            .get('amount__sum') or 0
        )

     
        this_month_saving = this_month_income - this_month_expenses

        expences = (
            Expences.objects.filter(user=request.user)
            .order_by('-date')[:5]
        )

        monthly_data = (
            Expences.objects
            .filter(user=request.user)
            .annotate(month=TruncMonth('date'))
            .values('month')
            .annotate(total=Sum('amount'))
            .order_by('month')
        )

        for item in monthly_data:
            months.append(item['month'].strftime('%b'))
            monthly_expenses.append(float(item['total']))

    context = {
        'total_expenses': total_expenses,
        'total_income': total_income,
        'balance': total_saving,
        'this_month_saving': this_month_saving,
        'expences': expences,
        'months': months,
        'monthly_expenses': monthly_expenses,
    }

    return render(request, 'pages/home.html', context)


def aboutus_view(request):
    return render(request, 'pages/about.html')