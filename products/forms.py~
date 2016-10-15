from django import forms
from django.contrib.auth.models import User
from products.models import Product
from datetimewidget.widgets import DateTimeWidget, DateWidget, TimeWidget 
from django.utils.datastructures import MultiValueDictKeyError

class PostForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('title', 'description', 'active', 'quantity','address', 'zip_Code', 'expire_date', )


class ProductForm(forms.Form):

    METHOD_OF_CONTACT = (
        ('EMAIL','Email'),
        ('CALL', 'Call'),
        ('TEXT', 'Text'),
    )
    
    title = forms.CharField(
        label='Title', widget=forms.TextInput(attrs={'placeholder': 'Enter title'})
    )
    
    description = forms.CharField(
        label='Description', widget=forms.Textarea(attrs={'cols': 22, 'rows': 2 ,'placeholder': 'Tell more about your donating item'})
    )   
   
    quantity = forms.IntegerField(
        label='Quantity', widget=forms.TextInput(attrs={'placeholder': 'No. of items you donating'})
    )
    zip_Code = forms.CharField(
        label='Zipcode', widget=forms.TextInput(attrs={'placeholder': 'Zipcode of your area'})
    )
    docfile = forms.FileField(required=False,
        label='Product Image '
    )
    address = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=METHOD_OF_CONTACT,label='Preferred Method of Contact',
    )
   
    expire_date = forms.DateTimeField(widget=DateTimeWidget(usel10n=True, bootstrap_version=3))

    active = forms.BooleanField(
        label='Are you sure to publish'
    )


