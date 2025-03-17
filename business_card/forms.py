import re

from django import forms
from .models import ContactInfo


class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactInfo
        fields = ['name', 'email', 'subject', 'message']
        labels = {
            'name': 'Imię',
            'email': 'E-mail',
            'subject': 'Temat',
            'message': 'Wiadomość',
        }
        error_messages = {
            'name': {'required': "Imię nie może być puste!"},
            'email': {'required': "Email nie może być pusty!", 'invalid': "Podaj poprawny adres e-mail"},
            'subject': {'required': "Temat nie może być pusty!"},
            'message': {'required': "Wiadomość nie może być pusta!"}
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')

        if len(name) < 2:
            raise forms.ValidationError("Imię musi mieć conajmniej 2 znaki!")

        if not name.replace(" ", "").isalpha():
            raise forms.ValidationError("Imię może zawierać tylko litery!")
        return name

    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_regex_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

        if not re.match(email_regex_pattern, email):
            raise forms.ValidationError("Podaj poprawny adres e-mail!")
        return email

    def clean_subject(self):
        subject = self.cleaned_data.get('subject')

        if len(subject) < 2:
            raise forms.ValidationError("Temat musi mieć conajmniej 2 znaki!")
        return subject

    def clean_message(self):
        message = self.cleaned_data.get('message')

        if len(message) < 10:
            raise forms.ValidationError("Wiadomość musi mieć conajmniej 10 znaków!")
        return message
