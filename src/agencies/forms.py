from django import forms
from .models import Agency


class AgencyProfileForm(forms.ModelForm):
    class Meta:
        model = Agency
        fields = '__all__'
