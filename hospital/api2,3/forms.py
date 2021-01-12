from django import forms
from .models import Client
from django.core.exceptions import ValidationError

class formshift(forms.ModelForm):
    start_time = forms.TimeField(widget=forms.TimeInput(format='%H:%M'))
    end_time = forms.TimeField(widget=forms.TimeInput(format='%H:%M'))

    class Meta():
        model = Client
        fields = '__all__'

    def clean_date(self):
        date = self.cleaned_data.get('date')
        if not date:
            raise ValidationError('This field is required')
        return date

    def clean_repeat_type(self):
        repeat_type = self.cleaned_data.get('repeat_type')
        if not repeat_type:
            raise ValidationError('This field is required')
        return repeat_type

    def clean_shift(self):
        shift = self.cleaned_data.get('shift')
        if not shift:
            raise ValidationError('This field is required')
        return shift

    def clean_end_time(self):
        end_time = self.cleaned_data.get('end_time')
        if not end_time:
            raise ValidationError('This field is required')
        return end_time


    def clean_start_time(self):
        start_time = self.cleaned_data.get('start_time')
        end_time = self.cleaned_data.get('end_time')
        if not start_time:
            raise ValidationError('This field is required')
        if start_time >= end_time:
            raise forms.ValidationError('Start time should be less than end time')
        return start_time



