from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate , login, logout




# Create your views here.
def signup(request):
    form = UserCreationForm()
    context = {'form': form}
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signin')


    return render(request, 'account/signup.html', context)
def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user=authenticate(username=username, password=password)
        if user :
            login(request, user)
            return redirect('home')

    context = {}
    return render(request, 'account/signin.html',context)

def signout(request):
    logout(request)
    return redirect('signin')
