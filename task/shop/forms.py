from django import forms
from .models import Order


class BikeOrderForm(forms.Form):
    name = forms.CharField(label='your name', max_length=100)
    surname = forms.CharField(label='your surname', max_length=100)
    phone_number = forms.CharField(label='your phone number', max_length=15)


class BikeForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'surname', 'phone_number']
