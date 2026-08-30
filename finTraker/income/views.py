from django.shortcuts import render, redirect, get_object_or_404
from .models import Income
from .forms import IncomeForm
from django.contrib.auth.decorators import login_required


@login_required(login_url=('signin'))
def add_income(request):

    if request.method == 'POST':
        form = IncomeForm(request.POST)

        if form.is_valid():
            income = form.save(commit=False)
            income.user = request.user
            income.save()

            return redirect('list_income')

    else:
        form = IncomeForm()

    return render(request, 'income/addincome.html', {'form': form})

@login_required(login_url=('signin'))
def list_income(request):

    incomes = Income.objects.filter(user=request.user)

    return render(
        request,
        'income/listincome.html',
        {'incomes': incomes}
    )

@login_required(login_url=('signin'))
def delete_income(request, id):

    income = get_object_or_404(
        Income,
        id=id,
        user=request.user
    )

    if request.method == 'POST':
        income.delete()
        return redirect('listincome')

    return render(
        request,
        'income/deleteincome.html',
        {'income': income}
    )