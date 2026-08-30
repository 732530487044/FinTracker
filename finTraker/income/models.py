from django.db import models
from django.contrib.auth.models import User


class Income(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    source = models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self):
        return self.title