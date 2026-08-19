from django.urls import path
from .views import home_view,aboutus_view
urlpatterns = [
    path('', home_view, name='home'),
    path('about/',aboutus_view ,name='about'),
]