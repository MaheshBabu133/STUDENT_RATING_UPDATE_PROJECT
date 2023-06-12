
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.core.mail import send_mail

from django.contrib.auth.decorators import login_required
from app.forms import *
from django.urls import reverse
from app.models import *

def register(request):
    d={'user':UserForm(),'student':StudentForm()}
    if request.method=="POST":
        UFO=UserForm(request.POST)
        SFO=StudentForm(request.POST)
        name=request.POST['name']
        print(name)
         
        if UFO.is_valid() and SFO.is_valid():
            NUFO=UFO.save(commit=False)
            password=UFO.cleaned_data['password']
            NUFO.set_password(password)

            NUFO.save()
            NSFO=SFO.save(commit=False)
            NSFO.username=NUFO
            NSFO.Name=name
            NSFO.save()

            send_mail('registration',
                'registration is done succssfully',
                'maheshbabuntr123@gmail.com',
                [NUFO.email],
                fail_silently=False
                )

            
            return HttpResponse("<h1>Your registration Done sucessfully</h1>")
        else:
            return HttpResponse("<h1> Your data is invalid  \n (OR) User already existed</h1>")
            


    return render(request,'register.html',d)




#For HR login with Name:Harshad Mobile number:Harshad Passoword:1234 Then only you get the Student Rating update Form

def user_login(request):


    if request.method=="POST":
        un=request.POST["un"]
        username=request.POST['name']
        password=request.POST['pw']
        UO=User.objects.filter(username=username)
        UO=UO[0]
        UN=StudentData.objects.filter(Name=un,username=UO)
        print(UN)
        if UN:
            AUO=authenticate(username=username,password=password)
            if AUO and AUO.is_active:
                login(request,AUO)
                request.session['username']=username

                UO=User.objects.get(username=username)

                

                return HttpResponseRedirect(reverse('student_data'))
            else:
                return HttpResponse(" <h1>Sorry sir this is invalid mobile number/password</h1>")
        else:
            return HttpResponse(" <h1>Sorry sir this is invalid Username</h1>")
    return render(request,'login_form.html')
        




@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('user_login'))




def forget_password(request):
    if request.method=='POST':
        un=request.POST['un']
        username=request.POST['username']
        password1=request.POST['pw1']
        password2=request.POST['pw2']
        print(un)
        if password1==password2:
            LUO=User.objects.filter(username=username)
            try:
                LUO=LUO[0]
            except:
                return HttpResponse("<h1>Sorry/sir mam User  doesnot exits</h1>")
            print(LUO)
            LSO=StudentData.objects.filter(username=LUO,Name=un)
            print(LSO)
            if LUO and LSO:
                UO=LUO
                UO.set_password(password1)
                UO.save()
                return HttpResponse("<h1>password change successfully</h1>")
            else:
                return HttpResponse("<h1>Sorry/sir mam User  doesnot exits</h1>")
        else:
   
            return HttpResponse("<h1>Password Doesn't mathch go back and try again</h1>")

    return render(request,'forget_password.html')

@login_required
def change_password(request):
    if request.method=='POST':
        password1=request.POST['pw1']
        password2=request.POST['pw2']
        username=request.session.get('username')
        UO=User.objects.get(username=username)
        if password1==password2 and password1!=0:
            UO.set_password(password1)
            UO.save()
            return HttpResponse('<h1>Your Password changed successfully</h1>')
        else:
            return HttpResponse('<h1>Passwoed Doesnt match go back and try again</h1>')
    return render(request,'change_password.html')


@login_required
def student_data(request):
    if request.session.get('username'):
        username=request.session.get('username')
        UFO=User.objects.get(username=username)
        try:
            SFO=StudentData.objects.get(username=UFO)
        except:
            return HttpResponse(" <h1>Sorry sir this is invalid username/password</h1>")
            
        RF=StudentRating.objects.filter(username=UFO)
        CO=Course.objects.all()
        TO=Theory.objects.all()
        CMO=Comunication.objects.all()
        COD=Coding.objects.all()
        print(SFO.cname)
        
        if request.method=="POST":
            username=request.POST['username']
            co=request.POST['course']
            cod=request.POST['coding']
            to=request.POST['theory']
            com=request.POST['comu']
            UO=User.objects.filter(username=username)
            CO=Course.objects.filter(cname=co)
            if UO:
                UOU=UO[0]
                COU=CO[0]
                try:
                    OBJ=StudentData.objects.get(username=UOU,cname=COU)
                except:
                    return HttpResponse("<h1>student and course doesnot match</h1>")
                if OBJ:
                    MO=StudentRating.objects.update_or_create(username=UOU,defaults={'cname':co,'coding':cod,'theory':to,'comminication':com})[0]
                    MO.save()
                    return HttpResponse("<h1>Rating Successfully Updated</h1>")    
            else:
                return HttpResponse("<h1>The User Does no exist</h1>")
           
    d={'username':username,'UFO':UFO,'SFO':SFO,'CO':CO,'TO':TO,'CMO':CMO,'COD':COD,'RF':RF}
    return render(request,'student_data.html',d)

   
