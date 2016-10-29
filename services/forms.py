from django import forms
from django.contrib.auth.models import User
from datetimewidget.widgets import DateTimeWidget, DateWidget, TimeWidget 
from services.models import Service

class ServiceForm(forms.Form):

    METHOD_OF_CONTACT = (
        ('EMAIL','Email'),
        ('CALL', 'Call'),
        ('TEXT', 'Text'),
    )

    title = forms.CharField(
        label='Title', widget=forms.TextInput(attrs={'placeholder': 'Provide service name'})
    )
 
    zipcode = forms.CharField(
       label='Title', widget=forms.TextInput(attrs={'placeholder': 'zipcode'})
    )   
    docfile = forms.FileField(
        label='Select Service Image'
    )
    description = forms.CharField(
        label='Description', widget=forms.Textarea(attrs={'cols': 22, 'rows': 2 ,'placeholder': 'Some details about your service'})
    )     
    contact_method = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=METHOD_OF_CONTACT,label='Preferred Method of Contact',
    )
    contact_info = forms.CharField(
        label='Contact info', widget=forms.TextInput(attrs={'placeholder': 'Zipcode of your area'})
    )


class OfferForm(forms.ModelForm):

    class Meta:
        model = Service
        fields = ('title', 'docfile', 'description', 'contact_method', 'contact_info')




