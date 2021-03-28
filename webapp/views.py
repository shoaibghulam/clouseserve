from django.shortcuts import render , HttpResponse , redirect
from django.views import View
from passlib.hash import django_pbkdf2_sha256 as handler
from django.contrib import messages
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Q
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
import datetime
import requests
from passlib.hash import django_pbkdf2_sha256 as handler
from webapp.models import *


class index(APIView):


    def get(self,request):

        return render(request,'index.html')

    
    def post(self,request):
        try:

            Name = request.POST['Name']
            Email = request.POST['Email']
            Mobile_Number = request.POST['Mobile_Number']
            Gender = request.POST['Gender']
            Question_1 = request.POST['Question_1']
            Question_2 = request.POST['Question_2']
            Question_3 = request.POST['Question_3']
            Question_4 = request.POST['Question_4']
            Question_5 = request.POST['Question_5']
            Question_6 = request.POST['Question_6']

            data = SignupForm(Name = Name,Email=Email,Mobile_Number=Mobile_Number,Gender=Gender,Question_1=Question_1,Question_2=Question_2,Question_3=Question_3,Question_4=Question_4,Question_5=Question_5,Question_6=Question_6)
            data.save()
            return redirect(f'output/{data.SignupFormId}')

        except Exception as e:
            print("error is ",e)
            return redirect('/')
        


class output(APIView):
    def get(self,request,id):
        fetchObj = SignupForm.objects.get(SignupFormId = id )
        fetchObj = SerSignupForm(fetchObj)
        message = {'status':'true','data':fetchObj.data}
        question1 = float(message['data']['Question_1'])
        question2 = float(message['data']['Question_2'])
        if question1 <= question2:
            status1 = "True"

        else:
            status1 = "False"


        if message['data']['Question_3'] == "agree":
            status2 = "True"

        else:
            status2 = "False"


        if message['data']['Question_4'] == "yes":
            status3 = "True"

        else:
            status3 = "False"

        if message['data']['Question_5'] == "1-5":
            status4 = "True"

        else:
            status4 = "False"

        
        if message['data']['Question_5'] == "6-15":
            status5 = "True"

        else:
            status5 = "False"

        if message['data']['Question_5'] == "16-29":
            status6 = "True"

        else:
            status6 = "False"

        if message['data']['Question_5'] == "30-50":
            status7 = "True"

        else:
            status7 = "False"

        if message['data']['Question_5'] == "None at all":
            status8 = "True"

        else:
            status8 = "False"

        if message['data']['Question_6'] == "Yes":
            status9 = "True"

        else:
            status9 = "False"


    
        obj = {'status1':status1,'status2':status2,'status3':status3,'status4':status4,'status5':status5,'status6':status6,'status7':status7,'status8':status8,'status9':status9}
        # return Response(obj)
        return render(request,'result.html',{'obj':obj})
        
