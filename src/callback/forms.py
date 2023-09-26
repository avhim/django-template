from django import forms
from .models import CallBack


input_css_class = "form-control"

class CallBackForm(forms.ModelForm):
    class Meta:
        model = CallBack
        exclude = ['url']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['name'].widget.attrs['placeholder'] = "Your name"
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = input_css_class

    def send_email():
        pass
