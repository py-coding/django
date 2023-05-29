from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import authenticate,login


def login(request):
    return render(request,'login.html')





def Signup(request):

    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email_id = request.POST['email_id']
        pass1   = request.POST['pass1']
        pass2   = request.POST['pass2']

        myuser = User.objects.create_user(username,email_id,pass1)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()

        messages.success(request,"your account successfuly created")

        return redirect('loginn.html')
    return render(request,"Signup.html")

def loginn(request):
    if request.method == "POST":
        username = request.POST['username']
        pass1    = request.POST['pass1']


        user = authenticate(username = username , pass1 = pass1)

        if user is not None:
            login(request,user)
            fname = user.firstname
            return render(request,'login.html',{'fname': fname})
        else:
            messages.error(request, "worng")
            return redirect('login')
            

    return render(request,'loginn.html')

def logout(request):
    return render(request,'logout.html')