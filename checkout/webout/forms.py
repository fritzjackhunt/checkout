from django import forms

class MyForm(forms.Form):

    first_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': 'John',
            'class': 'form-control'
        })
    )

    last_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': 'Doe',
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

    address = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': 'Billing Address',
            'class': 'form-control'
        })
    )

    amount = forms.CharField(
        max_length=4,
        widget=forms.TextInput(attrs={
            'placeholder': 'Amount',
            'class': 'form-control'
        })
    )
