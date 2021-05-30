from django.db import models




class contact(models.Model):
    contact_id=models.AutoField
    uname=models.CharField(max_length=20)
    pswrd=models.CharField(max_length=20)


    def __str__(self):
        return self.uname

# Create your models here.
