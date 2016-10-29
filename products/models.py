from __future__ import unicode_literals
import uuid
from django.db import models
from authtools.models import User
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from django.conf import settings
from datetime import datetime, timedelta
# Create your models here.

class Product(models.Model):
    EMAIL = 'Email'
    CALL = 'Call'
    TEXT = 'Text'
    
    METHOD_OF_CONTACT = (
        (EMAIL, 'Email'),
        (CALL, 'Call'),
        (TEXT, 'Text'),
        
    )
    user = models.ForeignKey(User)
    title  = models.CharField(max_length=120)
    zipcode = models.CharField(max_length=200,null=False)
    docfile = models.FileField(upload_to='Product/%Y/%m/%d', default='img/default_profile.png')
    #description = models.CharField(max_length=120)
    description = models.CharField(default=False, max_length=160)
    contact_method = models.CharField(max_length=6,
        choices=METHOD_OF_CONTACT,
        default=EMAIL,
    )
    contact_info = models.CharField(blank = True, max_length=160)
    date_created = models.DateTimeField(default=datetime.now()+timedelta(days=30))


      
    class Meta:
        verbose_name = ("title")
        verbose_name_plural = ("title")
        ordering = ("docfile",)

    def __unicode__(self):
        return self.docfile.path
