from django.db import models
from rest_framework import serializers
# Create your models here.


class SignupForm(models.Model):

    SignupFormId = models.AutoField(primary_key=True)
    Name=models.CharField(max_length=100, default="")
    Email=models.EmailField(max_length=100,default="")
    Mobile_Number = models.CharField(max_length=200, default="")
    Gender = models.CharField(max_length=255,default="")
    Question_1 =  models.CharField(max_length=255,default="")
    Question_2 = models.CharField(max_length=255,default="")
    Question_3 = models.CharField(max_length=255,default="")
    Question_4 = models.CharField(max_length=255,default="")
    Question_5 = models.CharField(max_length=255,default="")
    Question_6 = models.CharField(max_length=255,default="")



class SerSignupForm(serializers.ModelSerializer):
    class Meta:
        model = SignupForm
        
        fields = '__all__'