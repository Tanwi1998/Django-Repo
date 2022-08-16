from distutils.command.upload import upload
from pyexpat import model
from django.db import models

# Create your models here.

class usermaster(models.Model):
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=50)
    otp=models.IntegerField()
    role=models.CharField(max_length=50)
    is_active=models.BooleanField(False)
    is_verified=models.BooleanField(False)
    date=models.DateTimeField(auto_now_add=True)
    date_update=models.DateTimeField(auto_now_add=True)


class candidate(models.Model):
    user_id=models.ForeignKey(usermaster,on_delete=models.CASCADE)
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    contact=models.CharField(max_length=50)
    address=models.CharField(max_length=150)
    dob=models.CharField(max_length=50)
    country=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    gender=models.CharField(max_length=50)
    pincode=models.CharField(max_length=50,null=True)
    job_type=models.CharField(max_length=150,null=True)
    profile_pic=models.ImageField(upload_to="app/img/candidate")
    resume=models.ImageField(upload_to="app/resume/candidate",null=True)


class company(models.Model):
    user_id=models.ForeignKey(usermaster,on_delete=models.CASCADE)
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    company_name=models.CharField(max_length=100)
    address=models.CharField(max_length=150)
    contact=models.CharField(max_length=50)
    country=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    pincode=models.CharField(max_length=50,null=True)
    logo=models.ImageField(upload_to="app/img/company")
