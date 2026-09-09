from django.shortcuts import render,redirect
from django.db.models import Sum
from expences.models import Expences
from income.models import Income
from datetime import date
from django.db.models.functions import TruncMonth

def home_view(request):
    if not request.user.is_authenticated:
        return redirect('signin')
    total_expenses =int( Expences.objects.filter(user=request.user).aggregate(Sum('amount')).get('amount__sum') or 0)

    total_income = Income.objects.filter(user=request.user).aggregate(Sum('amount') ).get('amount__sum') or 0



    total_saving = int(total_income)-int(total_expenses)

    today=date.today()
    this_month_expences=Expences.objects.filter(user=request.user,date__year=today.year,date__month=today.month).aggregate(Sum('amount')).get('amount__sum') 

    this_month_income=Income.objects.filter(user=request.user,date__year=today.year,date__month=today.month).aggregate(Sum('amount')).get('amount__sum') 
    this_month_saving=0
    print(this_month_income,this_month_expences)
    if this_month_income != None and this_month_expences == None:
     
       this_month_saving = this_month_income
    if this_month_income != None and this_month_expences != None:
       this_month_saving = int(this_month_income)- int(this_month_expences)
    
    expences = Expences.objects.filter(user=request.user).order_by('-date')[:5  ]

    monthly_data = (
    Expences.objects
    .filter(user=request.user)
    .annotate(month=TruncMonth('date'))
    .values('month')
    .annotate(total=Sum('amount'))
    .order_by('month')
    )

    months = []
    monthly_expenses = []

    for item in monthly_data:
        months.append(item['month'].strftime('%b'))
        monthly_expenses.append(float(item['total']))
    context = {
        'total_expenses': total_expenses,
        'total_income': total_income,
        'balance': total_saving,
        'this_month_saving':this_month_saving,
        'expences':expences,
        'months': months,
        'monthly_expenses': monthly_expenses,
    }
    return render(request, 'pages/home.html',context)
def aboutus_view(request):
    return render(request, 'pages/about.html')