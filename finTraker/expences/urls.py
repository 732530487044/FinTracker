from django.urls import path
from .views import addexpences,listexpences,deleteExpences,updateExpences

urlpatterns = [
    path('addexpences/',addexpences,name='addexpences'),
    path('listexpences/',listexpences,name='listexpences'),
    path("deleteExpences.<int:id>/" , deleteExpences, name="deleteExpences"),
    path("updateexpences/<int:id>/" , updateExpences, name="updateExpences"),
]