from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class blogpost (models.Model):
    post_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=250,default="")
    author=models.CharField(max_length=250,default="")
    author_address=models.CharField(max_length=250,default="")
    author_mail=models.CharField(max_length=50,default="")
    contant=RichTextField()
    #contant=models.TextField(max_length=100000,default="")
    image=models.ImageField(upload_to="blog/images",default="")
    date=models.DateField()

    def __str__(self):
        return self.title
    