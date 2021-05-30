from django.contrib.auth.models import User
from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def handleSignup(request):
    print("Inside signup")
    if request.method=="POST":
        username=request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1= request.POST['password']
        pass2 = request.POST['password1']


        tmp={'first_name':fname,'last_name':lname}

        myuser=User.objects.create_user(username,email,pass1,**tmp)
        #myuser.first_name=fname
        #myuser.last_name=lname
        myuser.save()
        messages.success(request,"Your acoount has Successfully created")
        return redirect('home')

    else:
        return HttpResponse("404-Not Found")


def home(request):
    result=User.objects.all()
    return render(request,'login/users.html',{'users':result})

def handlelogin(request):
    if request.method=="POST":
        uname=request.POST['user']
        pswd=request.POST['pwd']

        user=authenticate(username=uname,password=pswd)

        if user is not None:
            login(request,user)
            messages.success(request,"Successfully logged in")
            return redirect(home)

        else:
            messages.error(request,"Invalid credentials!!!Please try again")
            return redirect('nothome')


    else:
        return HttpResponse("404-Not Found")

def handlelogout(request):
    logout(request)
    messages.success(request,"Successfully logged out")
    return redirect(out)


def nothome(request):
    msg="<H1>Successfully Logged Out</H1>"
    return HttpResponse(msg)

def out(request):
    msg="<H1>Thank You</H1>"
    return HttpResponse(msg)

def index(request):

    return render(request,'login/index.html')

def users(request):
    temp = {"users": [{"email": "email"}]}
    return render(request,'login/users.html',temp)
    #return HttpResponse("This is user page")


def profile(request):
    result=User.objects.all()
    return render(request,'login/profile.html',{'users':result})