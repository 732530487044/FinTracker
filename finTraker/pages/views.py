from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request, 'pages/home.html')
def aboutus_view(request):
    return render(request, 'pages/about.html')