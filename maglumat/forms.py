from django import forms
from phonenumber_field.formfields import PhoneNumberField

class gosulmak_form(forms.Form):
    at=forms.CharField(max_length=50,
                        widget=forms.TextInput(attrs={
                                'class':'form-control',
                                'placeholder':'At',
                            }))
    email=forms.EmailField(
                        widget=forms.EmailInput(attrs={
                                'class':'form-control',
                                'placeholder':'Email',
                            }))
    password=forms.CharField(max_length=8,
                        widget=forms.PasswordInput(attrs={
                                'class':'form-control',
                                'placeholder':'Açar söz',
                            }))
    phone=PhoneNumberField(
                        widget=forms.TextInput(attrs={
                                'class':'form-control',
                                'placeholder':'Telefon belgiňiz',
                            }))
