from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class RegularUser(models.Model):
    user_r = models.OneToOneField(User,on_delete=models.CASCADE)
    fb = models.URLField(blank=False)
    phone = models.CharField(max_length=11,default=0)
    city = models.CharField(max_length=20,blank=False)
    about_you = models.TextField(blank=True)
    photo = models.ImageField(upload_to="regular_user/")


    def __str__(self):
        return str(self.user_r)

class OrganizationUser(models.Model):
    user_o = models.OneToOneField(User,on_delete=models.CASCADE)
    o_name = models.CharField(max_length=30,blank=True)
    purpose = models.TextField(blank=False)
    web = models.URLField(blank=False)
    phone = models.CharField(max_length=11, default=0)
    city = models.CharField(max_length=20,blank=False)
    address = models.TextField(max_length=30,blank=False)
    photo = models.ImageField(upload_to="organization_user/", default='default.jpg')

    def __str__(self):
        return str(self.o_name)



