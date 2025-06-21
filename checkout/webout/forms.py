from django import forms
from .countries import COUNTRIES

class MyForm(forms.Form):

    full_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter your full name',
            'class': 'form-control'
        })
    )

    email = forms.EmailField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': 'Email Address',
            'class': 'form-control'
        })
    )

    card_number = forms.CharField(
        label='',
        max_length=19,
        widget=forms.TextInput(attrs={
            'placeholder': 'Card Number',
            'inputmode': 'numeric',
            'autocomplete': 'cc-number',
            'class': 'card-input',
            'id': 'card_number_input',
        })
    )
    
    expiry = forms.CharField(
        label='',
        max_length=5,
        widget=forms.TextInput(attrs={
            'placeholder': 'MM/YY',
            'inputmode': 'numeric',
            'autocomplete': 'cc-number',
            'class': 'card-input',
            'id': 'expiry_input',
        })
    )
    
    cvv = forms.CharField(
        label='',
        max_length=3,
        widget=forms.TextInput(attrs={
            'placeholder': 'CVC',
            'inputmode': 'numeric',
            'autocomplete': 'cc-number',
            'class': 'card-input',
        })
    )

    address1 = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': 'Address Line 1',
            'class': 'form-control'
        })
    )

    address2 = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': 'Address Line 2',
            'class': 'form-control'
        })
    )

    country = forms.ChoiceField(
        choices=COUNTRIES, 
        widget=forms.Select(attrs={
        'placeholder':'Select your country',
        'class':'form-control'
    }))

    amount = forms.CharField(
        max_length=4,
        widget=forms.TextInput(attrs={
            'placeholder': 'Amount',
            'class': 'form-control'
        })
    )
