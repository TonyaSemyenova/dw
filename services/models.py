from __future__ import unicode_literals
import uuid
from django.db import models
from authtools.models import User
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from django.conf import settings
# Create your models here.

class Service(models.Model):
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
    docfile = models.FileField(upload_to='Service/%Y/%m/%d',blank=True, null=True)
    description = models.CharField(default=False, max_length=160)
    zipcode = models.CharField(max_length=200,null=False)
    contact_method = models.CharField(max_length=6,
        choices=METHOD_OF_CONTACT,
        default=EMAIL,
    )
    contact_info = models.CharField(default=False, max_length=60)
    date_created = models.DateTimeField(default=timezone.now)

    
    class Meta:
        verbose_name = ("Service")
        verbose_name_plural = ("services")
    def __unicode__(self):
        return (self.title)

