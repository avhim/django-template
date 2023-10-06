from django import forms
from django.forms import inlineformset_factory, modelformset_factory
from ckeditor_uploader.widgets import CKEditorUploadingWidget
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


class TourUpdateForm(forms.ModelForm):
    class Meta:
        model = Tour
        exclude = ["user", "count_views"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['name'].widget.attrs['placeholder'] = "Your name"
        for field in self.fields:
            if field in ['active']:
                continue
            self.fields[field].widget.attrs['class'] = input_css_class


class TourDescriptionDayForm(forms.ModelForm):
    base_textarea_id = "id_day_description"

    class Meta:
        model = TourDescriptionDay
        exclude = ["tour"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['name'].widget.attrs['placeholder'] = "Your name"
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = input_css_class
        self.textarea_id_counter = 0
        self.fields['description'].widget = CKEditorUploadingWidget(attrs={'id':self.get_textarea_next_id})

    def get_textarea_next_id(self):
        result = self.base_textarea_id + str(self.textarea_id_counter)
        self.textarea_id_counter += 1
        return result


TourDescriptionDayModelFormSet = modelformset_factory(
    TourDescriptionDay,
    form=TourDescriptionDayForm,
    exclude=["tour"],
    extra=0,
    can_delete=True
)

TourDescriptionDayInlineFormSet = inlineformset_factory(
    Tour,
    TourDescriptionDay,
    form=TourDescriptionDayForm,
    formset=TourDescriptionDayModelFormSet,
    exclude=["tour"],
    extra=0,
    can_delete=True
)


class TourDayQuotaForm(forms.ModelForm):
    class Meta:
        model = TourDayQuota
        exclude = ["tour"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['name'].widget.attrs['placeholder'] = "Your name"
        for field in self.fields:
            if field in ['active']:
                continue
            self.fields[field].widget.attrs['class'] = input_css_class
