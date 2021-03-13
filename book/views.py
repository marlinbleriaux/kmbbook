from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponseRedirect
from .forms import LoginForm
from .forms import StudentProfileForm , EmployeeProfileForm
from book.models import Personne
from  book.models import Etudiant, Employe



def get_logged_user_from_request(request):
    if 'logged_user_id' in request .session: 
       logged_user_id = request.session['logged_user_id ']
       # On cherche un etudi ant
       if len(Etudiant .objects . filter(id=logged_user_id)) ==1:
          return Etudiant .objects .get(id=logged_user_id)
       # On cherche un Employe
       elif len(Employe .objects . filter(id=logged_user_id)) ==1: 
          return Employe .objects .get(id=logged_user_id)
       # Si on n'a rien trouve
       else:
          return None 
    else:
          return None


def welcome(request):
    return  render(request,"welcome.html")
    
    
#    logged_user = get_logged_user_from_request(request)
 #   if logged_user :
 #     return render(request,'welcome.html',{'logged_user' : logged_user})
  #  else:
  #    return HttpResponseRedirect ('/login') 

def login(request):
    #Teste si le formulaire a été envoyé
    if request.method == "POST":
        form = LoginForm(request.POST) 
        if form .is_valid(): 
            user_email = form.cleaned_data['email'] 
            logged_user = Personne.objects.get(courriel=user_email) 
            request.session['logged_user_id'] = logged_user.id
            return render(request,'welcome.html')
            
    else:
        form = LoginForm()
        return render(request,'login.html', {'form':form})

def register(request) :
    if len(request.GET) > 0:
        form = StudentProfileForm(request.GET)
        if form.is_valid() :
          form.save(commit=True)
          return HttpResponseRedirect('/login')
        else :
           return render (request,'login.html', {'form' : form})
    else:
        form = StudentProfileForm()
    return render(request,'user_profile.html', {'form' : form}) 

def register(request) :
    if len(request.GET) > 0 and 'profileType' in request.GET: 
        studentForm = StudentProfileForm(prefix="st")
        employeeForm = EmployeeProfileForm(prefix="em")
        if request.GET['profileType'] == 'student': 
            studentForm = StudentProfileForm(request.GET, prefix="st")
            if studentForm.is_valid() : 
               studentForm.save(commit=True)
               return HttpResponseRedirect(' /login ')
        elif request.GET['profilelype'] == 'employee' :
            employeeForm = EmployeeProfileForm(request.GET, prefix="em")
            if employeeForm.is_valid() :
                employeeForm.save(commit=True)
                return HttpResponseRedirect('/login')
        #Le formulaire envoyé n'est pas valide
        return render(request,'user_profile.html ' ,{'studentForm' : studentForm ,'employeeForm': employeeForm}) 
    else: 
        studentForm = StudentProfileForm(prefix="st")
        employeeForm = EmployeeProfileForm(prefix="em")
    return render(request,'user_profile.html ', {'studentForm ': studentForm, 'employeeForm' : employeeForm})       