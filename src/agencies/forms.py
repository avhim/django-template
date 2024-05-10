from django import forms
from django.contrib.auth.models import Group
from allauth.account.forms import SignupForm

from .models import Agency


class MyCustomSignupForm(SignupForm):

    def save(self, request):
        # Ensure you call the parent class's save.
        # .save() returns a User object.
        user = super(MyCustomSignupForm, self).save(request)
        # Add your own processing here.
        agency = request.session.get('user_type')
        group = agency or "Default"
        g = Group.objects.get(name=group)
        user.groups.add(g)
        # You must return the original result.
        return user


class AgencyProfileForm(forms.ModelForm):
    class Meta:
        model = Agency
        exclude = ['user',]
