from django.contrib.auth.models import User
from django.forms import ValidationError
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from flask import request
from rest_framework.response import Response
from rest_framework import status
from student_application.models import  login_page, register_page, Student_Info
from rest_framework.views import APIView


class Save_Student_Info(APIView):
    def post(self, request):
        if request.method == "POST":
            name = request.POST.get('name')
            age = request.POST.get('age')
            student_class = request.POST.get('student_class') 
            tamilmarks = request.POST.get('tamilmarks')
            englishmarks = request.POST.get('englishmarks')
            sciencemarks = request.POST.get('sciencemarks')
            mathsmarks = request.POST.get('mathsmarks')
            socialmarks = request.POST.get('socialmarks')
            
            try:
                student_obj = Student_Info.objects.create(
                    name=name,
                    age=age,
                    student_class=student_class,
                    tamilmarks=tamilmarks,
                    englishmarks=englishmarks,
                    sciencemarks=sciencemarks,
                    mathsmarks=mathsmarks,
                    socialmarks=socialmarks
                )
                student_obj.save()
                return HttpResponseRedirect('/table/')
            except Exception as e:
                return render(request, 'index.html', {'error_message': str(e)})

class TableView(APIView):
    def get(self, request):
        Student_Table = Student_Info.objects.all()
        return render(request, 'table.html', {'student_info': Student_Table})



class save_register_page(APIView):
    def post(self, request):
        if request.method == 'POST':
            print(request)
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            username = request.POST.get('username')
            password = request.POST.get('password')

            register_user_obj = register_page.objects.filter(username=username)

            if len(register_user_obj) > 0:
                messages.info(request, "Username already taken!")
                return redirect('/register/')

            register_page(
                first_name=first_name,
                last_name=last_name,
                username=username,
                password=password
            ).save()

            messages.info(request, "Account created successfully!")
            return redirect('/login/')

        return render(request, 'register.html')
    

class UserLogin(APIView):
    def post(self,request):
        print(request)
    
        if request.method == "POST":
          username = request.POST.get('username')
          password = request.POST.get('password')

        
        try:
            user_data = register_page.objects.get(username=username,password=password)
            if user_data:
                return Response('success')
          
        except register_page.DoesNotExist:
            return Response ('error')
                 
        # print(user_data)



        
        

           
     
   
    






           
    