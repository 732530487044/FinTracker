from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Expences(models.Model):

    CATEGORY_CHOICES = (
        ('food', 'Food'),
        ('electronic', 'Electronic'),
        ('bill', 'Bill'),
        ('medical', 'Medical'),
        ('entertainment', 'Entertainment'),
        ('other', 'Other'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    amount = models.FloatField()
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES
    )
    date = models.DateTimeField(auto_now_add=True)

