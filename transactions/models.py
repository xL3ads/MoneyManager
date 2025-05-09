from random import choices

from django.contrib.auth.models import User
from django.db import models

from categories.models import UserCategory

# Create your models here.

class UserTransactions(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    category = models.ForeignKey(UserCategory, null = True, blank = True, on_delete = models.SET_NULL)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Aici o sa stocam din variabila date luna si anu unde mai departe o sa le folosim pentru statisitici
    month = models.IntegerField(null = True, blank = True)
    year = models.IntegerField(null = True, blank = True)

    def __str__(self):
        return f"Transaction: {self.amount} - {self.category.name}"
