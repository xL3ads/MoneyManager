from django import forms
import datetime

from django.views.generic import CreateView

from categories.models import UserCategory
from transactions.models import UserTransactions

class TransactionForm(forms.ModelForm):
    class Meta:
        model = UserTransactions
        fields = ['category', 'amount', 'date', 'description']

        widgets = {
            'category': forms.Select(attrs={'class': 'form-control' }),
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Amount of money'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

    # Vreau sa imi ia doar acele categorii create de utilizator
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        if user:
            self.fields['category'].queryset = UserCategory.objects.filter(user=user)
        else:
            self.fields['category'].queryset = UserCategory.objects.none()

    def clean(self):
        cleaned_data = self.cleaned_data
        amount = cleaned_data['amount']
        date = cleaned_data['date']

        # verificam daca suma introdusa este mai mica ca 0
        if amount <= 0:
            msg = 'The amount of money must be greater than zero.'
            self.add_error('amount', msg)

        # verificam ca daca sa nu fie in viitor
        if date > datetime.datetime.now().date():
            msg = 'The date you entered is not valid.'
            self.add_error('date', msg)

        return cleaned_data

class TransactionUpdateForm(forms.ModelForm):
    class Meta:
        model = UserTransactions
        fields = ['category', 'amount', 'description']

        widgets = {
            'category': forms.Select(attrs={'class': 'form-control' }),
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Amount of money'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
        }