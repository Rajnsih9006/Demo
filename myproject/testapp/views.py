from django.shortcuts import render,redirect
from django.contrib import auth
# from.models import Contact
from django.http import HttpResponse

# Create your views here.


# Create .models import here.
def home(request):
    return HttpResponse("<H1>welcome to home page</H1>")

def signup(request):
    if request.method == "POST":
        fname = request.POST.get("firstname")
        lname = request.POST.get("lastname")
        eml = request.POST.get("email")
        mob = request.POST.get("mobile")
        username = request.POST.get("username")
        password = request.POST.get("password")
        print("my firstname is {}".format(fname))
        print("my lastname is {}".format(lname))
        print("my email is {}".format(eml))
        print("my Number is {}".format(mob))
        print("my username is {}".format(username))
        print("my password is {}".format(password))
        obj = Contact(20, fname, lname, eml, mob, username, password)
        obj.save()
        result =Contact.objects.all()
        print(result)
        return render(request, 'testapp/signup.html')


def login(request):
    if request.method == "post":
        username1 = request.POST.get("username")
        password1 = request.POST.get("password")
        print("my username is {}".format(username1))
        print("my password is {}".format(password1))
        x = auth.authenticate(username=username1, password=password1)
        if x is None:
            return HttpResponse("<H1>Invalid username or password</H1>")
        else:
            return redirect('home')
        obj = Login(20, username1, password1)
        obj.usname = username1
        obj.pswd = password1
        obj.save()
        result = Contact.objects.all()
        print(result)
    else:
        return HttpResponse('Not Found')


def about(request):
    return HttpResponse("<H1>about page</H1>")
