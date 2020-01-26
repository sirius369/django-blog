from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

class RegistrationForm(forms.Form):
    username = forms.CharField(label = "Username", max_length = 100, min_length = 3, widget = forms.TextInput(attrs={'class' : 'text_input', 'placeholder' : 'Username'}))
    email = forms.EmailField(widget = forms.TextInput(attrs={'class' : 'text_input', 'placeholder' : 'Email'}))
    password = forms.CharField(label = "Password", max_length = 100, min_length = 5, widget = forms.PasswordInput(attrs = {'class' : 'text_input', 'id' : 'pass', 'placeholder' : 'Password'}))
    repeat_password = forms.CharField(label = "Repeat Password", max_length = 100, min_length = 5, widget = forms.PasswordInput(attrs = {'class' : 'text_input', 'id' : 'rpass','placeholder' : 'Repeat password'}))

    def clean_email(self):
        email = self.cleaned_data['email']
        qs = User.objects.filter(email = email)
        if qs.exists():
            raise forms.ValidationError(_("Email is already registered!"), code = "email_error")
        return email

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password')
        password2 = cleaned_data.get('repeat_password')
        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError(_("Passwords don't match"), code = "password_match_error")

    def save(self, commit = True):
        user = super(RegistrationForm, self).save(commit = False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
