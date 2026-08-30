from django.urls import path
from .views import add_income,list_income, delete_income

urlpatterns = [
    path('addincome/',add_income, name='add_income'),
    path('listincome/',list_income, name='list_income'),
    path('deleteincome/<int:id>/', delete_income, name='delete_income'),
]
