from django import forms
from .models import Client


class CreateClientForm(forms.ModelForm):
    class Meta:
        model = Client
        feilds = '__all__'
