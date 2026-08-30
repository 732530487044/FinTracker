from django.shortcuts import render,redirect
from .forms import ExpencesForm
from .models import Expences
from django.contrib.auth.decorators import login_required

@login_required(login_url='signin')
def addexpences(request):
    form = ExpencesForm()
    if request.method == 'POST':
        form = ExpencesForm(request.POST)
        if form.is_valid():
           expence= form.save(commit=False)
           expence.user=request.user
           expence.save()
           return redirect('listexpences')
    return render(request,'expences/add_expences.html',{'form':form})

@login_required(login_url='signin')
def listexpences(request):
    expences=Expences.objects.filter(user=request.user)
    context = {'expences':expences}
    return render(request,'expences/list_expences.html',context)

@login_required(login_url='signin')
def deleteExpences(request,id):
    expences=Expences.objects.get(id=id)
    if request.method == 'POST':
        expences.delete()
        return redirect('listexpences')
    context = {'expences': expences}
    return render(request,'expences/delete_expences.html',context)

@login_required(login_url='signin')
def updateExpences(request,id):
    expences=Expences.objects.get(id=id)
    form=ExpencesForm(instance=expences)
    if request.method == 'POST':
        form=ExpencesForm(request.POST,instance=expences)
        if form.is_valid():
            form.save()
            return redirect('listexpences')
    context = {'form':form}
    return render(request,'expences/update_expences.html',context)
