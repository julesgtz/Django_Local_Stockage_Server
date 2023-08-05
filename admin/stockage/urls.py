from django.urls import path
from . import views

#"" register + login, si c'est bon renvoi vers "/stockage/"
#"/stockage/" sera l'endroit pour recuperer les fichiers / dossiers/ images etc etc
#"/stockage/add/" permettra d'ajouter un nouveau fichier / dossiers etc etc
#faut qu'on puisse voir qui a ajouter quoi et quand
#/ account pour changer son blz

urlpatterns = [
    path('', views.login_rq),
    path('register/', views.register_rq),
    path('logout/', views.logout_rq),
    path('stockage/', views.stockage),
    path('add/', views.add)
]
