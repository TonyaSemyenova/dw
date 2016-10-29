from django import forms
from django.contrib.auth.models import User
from products.models import Product
from datetimewidget.widgets import DateTimeWidget, DateWidget, TimeWidget 
from django.utils.datastructures import MultiValueDictKeyError

class PostForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('title','zipcode', 'description', 'contact_method', 'contact_info', 'docfile'  )


class ProductForm(forms.Form):

    METHOD_OF_CONTACT = (
        ('EMAIL','Email'),
        ('CALL', 'Call'),
        ('TEXT', 'Text'),
    )
    
    title = forms.CharField(
        label='Title', widget=forms.TextInput(attrs={'placeholder': 'Enter title'})
    )
    zipcode = forms.CharField(
       label='Title', widget=forms.TextInput(attrs={'placeholder': 'zipcode'})
    )
    
    description = forms.CharField(
        label='Description', widget=forms.Textarea(attrs={'cols': 22, 'rows': 2 ,'placeholder': 'Tell more about your donating item'})
    )   
   
    docfile = forms.FileField(required=False,
        label='Product Image '
    )
    contact_method = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=METHOD_OF_CONTACT,label='Preferred Method of Contact',
    )
    contact_info = forms.CharField(
        label='Contact info', widget=forms.TextInput(attrs={'placeholder': 'Zipcode of your area'})
    )



