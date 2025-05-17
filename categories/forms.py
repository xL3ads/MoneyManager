from django import forms

from categories.models import UserCategory


class CategoryForm(forms.ModelForm):
    class Meta:
        model = UserCategory
        fields = '__all__'
        exclude = ('user',)

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Category Name'}),
            'is_income': forms.Select(attrs={'class': 'form-control'}),
        }

