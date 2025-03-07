import re

from django import forms
from .models import ContactInfo


class ContactMessageForm(forms.ModelForm):
    email = forms.EmailField(error_messages={'invalid': "Podaj poprawny adres e-mail"})
    # MUSZĘ RĘCZNIE ZMIENIĆ

    class Meta:
        model = ContactInfo
        fields = ['name', 'email', 'subject', 'message']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.required = False

    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_regex_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

        if not re.match(email_regex_pattern, email):
            raise forms.ValidationError('Podaj poprawny adres e-mail!')
        return email