
from django.shortcuts import render

# Create your views here.
from django.db.models import Q

from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic import CreateView,UpdateView
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

        if UFO.is_valid() and SFO.is_valid():
            NUFO=UFO.save(commit=False)
            password=UFO.cleaned_data['password']
            NUFO.set_password(password)

            NUFO.save()
            NSFO=SFO.save(commit=False)
            NSFO.username=NUFO
            NSFO.save()

            send_mail('registration',
                'registration is done succssfully',
                'maheshbabuntr123@gmail.com',
                [NUFO.email],
                fail_silently=False
                )

            
            return HttpResponse("Registrain Done suucess fully")
        else:
            return HttpResponse("the data is invalid")

    return render(request,'register.html',d)


def user_login(request):


    if request.method=="POST":

        username=request.POST['name']
        password=request.POST['pw']
        AUO=authenticate(username=username,password=password)
        if AUO and AUO.is_active:
            login(request,AUO)
            request.session['username']=username

            UO=User.objects.get(username=username)

            

            return HttpResponseRedirect(reverse('student_data'))
        else:
            return HttpResponse(" <h1>Sorry sir this is invalid username/password</h1>")
    return render(request,'login_form.html')
        




@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('user_login'))




def forget_password(request):
    if request.method=='POST':
        username=request.POST['username']
        password1=request.POST['pw1']
        password2=request.POST['pw2']
        if password1==password2 and password1!=0:
            LUO=User.objects.filter(username=username)
            if LUO:
                UO=LUO[0]
                UO.set_password(password1)
                UO.save()
                return HttpResponse("<h1>password change successfully</h1>")
            else:
                return HttpResponse("<h1>Sorry/sir mam User doesnot exits</h1>")
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
        SFO=StudentData.objects.get(username=UFO)
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

   