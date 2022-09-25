from django.db import models

# Create your models here.
class questions_base(models.Model):
    sl_no=models.AutoField(primary_key=True)
    question=models.CharField(max_length=500,default="")
    option1=models.CharField(max_length=100,default="")
    option2=models.CharField(max_length=100,default="")
    option3=models.CharField(max_length=100,default="")
    option4=models.CharField(max_length=100,default="")
    correct=models.CharField(max_length=1,default="")
    
    def __str__(self):
        return self.question