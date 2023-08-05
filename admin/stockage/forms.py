from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . import models
from django.utils.translation import gettext_lazy as _


# Create your forms here.

class NewUserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(NewUserForm, self).__init__(*args, **kwargs)
        del self.fields['password2']
        self.fields['password1'].help_text = None
        self.fields['username'].help_text = None


    class Meta:
        model = User
        fields = ("username", "password1")

class LoginForm(forms.Form):
    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)

class FilesForm(ModelForm):
    class Meta:
        model = models.Files
        fields = ('name','file',)
        labels = {
            'name': _('Donnez un nom a votre fichier'),
            'file': _('Votre fichier'),
        }