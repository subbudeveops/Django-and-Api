from django import forms
from .models import Student


class Studentform(forms.ModelForm):
    def celan_age(self):
        inputage = self.cleaned_data['age']
        if inputage == 25:
            raise forms.ValidationError('The minimum age should be  25')
        return inputage

    class Meta:
        model = Student
        fields = '__all__'
