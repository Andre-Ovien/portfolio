from django import forms
from .models import ContactForm


class UserForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = '__all__'