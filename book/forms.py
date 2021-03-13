from django import forms 
from book.models import Personne
from book.models import Etudiant 
from book.models import Employe

class LoginForm (forms.Form) : 

    email = forms.EmailField(label='Courriel ')
    password = forms.CharField(label='Mot de passe',widget = forms.PasswordInput)
   
   
    def clean(self): 
        cleaned_data = super (LoginForm, self).clean() 
        email = cleaned_data.get("email") 
        password = cleaned_data .get("password") 
        #Vérifie que les deux champs sont valides
        if email and password : 
            if password != 'sesame' or email != ' pierre@lxs.be': 
                raise forms.ValidationError ("Adresse de courriel ou mot de passe erroné.") 
        if email and password :
            result = Personne.objects.filter(mot_de_passe = password,courriel = email)

        if len(result) != 1: 
            raise forms.ValidationError("Adresse de courriel ou mot de passe erroné(e). ")                                                        
        
        
        return cleaned_data   

class StudentProfileForm(forms.ModelForm): 
        class Meta : 
            model = Etudiant
            exclude = ( 'amis',)


class EmployeeProfileForm(forms.ModelForm):
        class Meta:
            model = Employe
            exclude = ('amis',)            
           