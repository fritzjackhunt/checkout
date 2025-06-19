from django import forms

class MyForm(forms.Form):
    card_no = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': '0123 4567 8910',
            'class': 'form-control'
        }))
    
    expiry_date = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': '01/12',
            'class': 'form-control'
        }))
    
    cvv = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': '123',
            'class': 'form-control'
        }))
