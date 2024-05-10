from django import forms
from .models import CallBack
from .tasks import send_notification_mail

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

    def send_email(self,name=None, phone=None, url=None):
        msg = f' Пользователь имя: {name} \n номер телефона: {phone} \n оставил заявку на странице {url} \n в '
        send_notification_mail.delay(msg)
