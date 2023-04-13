from django import forms
from django.contrib.auth import get_user_model
from django_countries.widgets import CountrySelectWidget
from django_countries import countries
from .models import User,Instagram


USER = get_user_model()


class RegisterForm(forms.ModelForm):
        confirm_password = forms.CharField(label='*CONFIRM PASSWORD', label_suffix="", max_length=50, widget=forms.PasswordInput(attrs={
                'class': 'form-control',
    }))
        password = forms.CharField(label='*PASSWORD', label_suffix="", max_length=50, widget=forms.PasswordInput(attrs={
                'class': 'form-control',
    }))
        country = forms.ChoiceField(label='*COUNTRY', choices=countries, label_suffix="", widget=CountrySelectWidget(attrs={
        'class': 'selectpicker form-control',
        
    }))
        first_name = forms.CharField(label='*FIRST NAME', label_suffix="", max_length=50, widget=forms.TextInput(attrs={
        'class': 'form-control',
        
    }))
        last_name = forms.CharField(label='*LAST NAME', label_suffix="", max_length=50, widget=forms.TextInput(attrs={
        'class': 'form-control',
        
    }))
        email = forms.EmailField(label='*EMAIL', label_suffix="", max_length=40, widget=forms.EmailInput(attrs={
        'class': 'form-control',
    }))
        phone = forms.CharField(label='*PHONE', label_suffix="", max_length=20, widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))
        username = forms.CharField(label='*USERNAME', label_suffix="", max_length=20, widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))

        class Meta:
            model = USER
            fields = (
                'first_name',
                'last_name',
                'username',
                'email',
                'phone',
                'password',
                'confirm_password',
                'country' 
            )
            widgets = {
                'password': forms.PasswordInput(attrs={
                    'class': 'form-control'
                })
            }

        def clean(self):
            data = self.cleaned_data
            print(data)
            if data['password'] != data['confirm_password']:
                raise forms.ValidationError("Password and confirm_password does not match")
            return super().clean()
        





