from django.contrib.auth.models import User
from django.db import models

# Create your models here.

is_income_choices = [
    (True, 'Income'),
    (False, 'Expense'),
]

class UserCategory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    is_income = models.BooleanField(choices=is_income_choices,default=False)  # Venituri vs Cheltuieli
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Category: {self.name} - Type: {'Income' if self.is_income else 'Expense'}"