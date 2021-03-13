from django.contrib import admin

from book.models import Faculte, Campus, Fonction,Cursus, Employe, Etudiant, Message

admin.site.register(Faculte)
admin.site.register(Campus)
admin.site.register(Fonction)
admin.site.register(Cursus)
admin.site.register(Employe)
admin.site.register(Etudiant)
admin.site.register(Message)

