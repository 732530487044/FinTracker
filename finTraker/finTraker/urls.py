
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('pages.urls')),
    path('account/', include('account.urls')),
    path('expences/', include('expences.urls')),
    path('income/', include('income.urls')),
]
