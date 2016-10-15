from __future__ import unicode_literals
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions
from django.contrib.auth import get_user_model
from . import models
from django.utils.translation import ugettext_lazy as _


User = get_user_model()


class UserForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Field('name'),
            Field('city', lable="City"),
            Field('zipfield', lable="Postal code"),            
            )

    class Meta:
        model = User
        fields = ['name','city','zipfield']
        labels = {
            'city': _('City'),
            'zipfield': _('Postal Code')
 }



class ProfileForm(forms.ModelForm):
    bio = forms.CharField(widget=forms.Textarea(attrs={'cols': 22, 'rows': 2}))
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Field('picture'),
            Field('bio'),
            Field('zipcode'),

            )

    class Meta:
        model = models.Profile
        fields = ['picture', 'bio']


class SignupForm(forms.Form):
    name = forms.CharField(max_length=30, label='Name')
    zipfield = forms.CharField(max_length=30, label='Zipcode')

    def signup(self, request, user):
        user.name = self.cleaned_data['name']
        user.zipfield = self.cleaned_data['zipfield']
        user.save()

    
