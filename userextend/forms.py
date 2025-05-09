from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class AuthenticationNewForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({'class':'form-control', 'placeholder':'Username'})
        self.fields['password'].widget.attrs.update({'class':'form-control', 'placeholder':'Password'})

class UserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

    def clean(self):
        cleaned_data = self.cleaned_data

        # Validare pentru email. In cazul in care exista un utilizator cu acelasi EMAIL
        get_email = cleaned_data.get('email')

        user_email_filter = User.objects.filter(email=get_email)
        if user_email_filter:
            msg = 'This email is already in use.'
            self.add_error('email', msg)
        # ------------------------------------------------------------------------------

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'class':'form-control', 'placeholder':'First Name'})
        self.fields['last_name'].widget.attrs.update({'class':'form-control', 'placeholder':'Last Name'})
        self.fields['email'].widget.attrs.update({'class':'form-control', 'placeholder':'Email'})
        self.fields['password1'].widget.attrs.update({'class':'form-control', 'placeholder':'Password'})
        self.fields['password2'].widget.attrs.update({'class':'form-control', 'placeholder':'Confirm Password'})

