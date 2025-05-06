from django.db import models

# Create your models here.

class UserCategory(models.Model):
    name = models.CharField(max_length=100)
    is_income = models.BooleanField(default=False)  # Venituri vs Cheltuieli
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Category: {self.name} - Type: {'Income' if self.is_income else 'Expense'}"