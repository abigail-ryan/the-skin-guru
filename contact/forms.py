from .models import ContactForm
from django import forms


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ('name', 'email', 'message')
