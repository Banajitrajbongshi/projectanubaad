from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class recieve_content(models.Model):
    name=models.CharField(max_length=128)
    email=models.CharField(max_length=128)
    address=models.CharField(max_length=128)
    content=RichTextField() 

    def __str__(self):
        return self.name
        