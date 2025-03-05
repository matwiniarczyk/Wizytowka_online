from django import forms
from .models import ContactInfo


class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactInfo
        fields = ['name', 'surname','email', 'subject', 'message']