

from django.db import models


class Faculte(models.Model):
    nom= models.CharField(max_length=30)
    couleur= models.CharField(max_length=6)
    # permet de lire et d'afficher le contenut dans la bd

    def  __str__(self):
        return self.nom
    
class Personne (models.Model ): 
    matricule = models.CharField(max_length=10)
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)
    date_de_naissance = models.DateField()
    courriel = models.EmailField()
    tel_fixe = models.CharField(max_length=20)
    tel_mobile = models.CharField(max_length=20)
    mot_de_passe = models.CharField(max_length=32)
    amis = models.ManyToManyField("self")
    faculte = models.ForeignKey(Faculte,on_delete=models.CASCADE)
    type_de_personne = 'generic'
    def __str__(self):
        return self.prenom + " " + self.nom

class Message(models.Model):
    auteur = models.ForeignKey(Personne,on_delete=models.CASCADE) 
    contenu = models.TextField()
    date_de_publication = models.DateField() 
    def __str__(self) :
        if len(self.contenu) > 20:
            return self.contenu[:19] + " "
        else:
            return self.contenu
    

class Campus (models.Model):
    nom = models.CharField(max_length=30)
    adresse_postale = models.CharField(max_length=60)
    def __str__(self):
        return self.nom
class Fonction (models.Model):
    intitule = models.CharField(max_length=30)
    
    def __str__(self):
        return self.intitule

class Cursus (models.Model):
    intitule = models.CharField(max_length=30)
    
    def __str__(self):
        return self.intitule

class Employe(Personne):

    bureau = models.CharField(max_length=30)
    campus = models.ForeignKey(Campus,on_delete=models.CASCADE)
    fonction= models.ForeignKey(Fonction,on_delete=models.CASCADE)
    type_de_personne = 'employee'
class Etudiant(Personne):

    cursus = models.ForeignKey(Cursus,on_delete=models.CASCADE)
    annee = models.IntegerField()   
    type_de_personne = 'student'


     