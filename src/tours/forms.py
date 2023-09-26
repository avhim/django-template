from django import forms
from tours.models import Tour, TourDayQuota, TourDescriptionDay


input_css_class = "form-control"

class TourForm(forms.ModelForm):
    class Meta:
        model = Tour
        exclude = ["user", "count_views"]
        # fields = '__all__'


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['name'].widget.attrs['placeholder'] = "Your name"
        for field in self.fields:
            if field in ['active']:
                continue
            self.fields[field].widget.attrs['class'] = input_css_class


class TourDescriptionDayForm(forms.ModelForm):
    class Meta:
        model = TourDescriptionDay
        exclude = ["tour"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['name'].widget.attrs['placeholder'] = "Your name"
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = input_css_class
