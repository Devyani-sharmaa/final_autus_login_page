from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
import random,string 

from django.http import HttpResponse
from django.shortcuts import redirect, render
# from .forms import MyForm

# Create your views here.
@login_required(login_url='login')
def HomePage(request):
    return render (request,'home.html',{"cap":str_num})

def SignupPage(request):
    num=random.randrange(1022,9899)
    global str_num
    str_num=str(num)
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        captcha=request.POST.get('cap')

        if  str_num==str(captcha):
            return HttpResponse("FORM")
        else:
            return HttpResponse("captcha not matches")
    
 
        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
        



    return render (request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')




# def test(request):
#     form=MyForm()

#     return render(request,'captcha/home.html',{'form':form})

# def submit(request):
#     if request.method == 'POST':
#         form=MyForm(request.POST)
#         if form.is_valid():
#             name=request.POST['fullname']
#             email=request.POST['email']
#             print('success')
#             print(name)
#             print(email)
#             return HttpResponse("Thankyou for submiting this form")
#         else:
#             print('fail')
#     return redirect(test)

