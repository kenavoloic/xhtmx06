from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Pages publiques
    path('', views.index, name='index'),
    
    # Authentication
    path('connexion/', auth_views.LoginView.as_view(template_name='configurations/pages/connexion.html'), name='connexion'),
    path('deconnexion/', auth_views.LogoutView.as_view(), name='deconnexion'),
    
    # Pages protégées
    path('accueil/', views.accueil, name='accueil'),
    path('htmx-example/', views.htmx_example, name='htmx_example'),
    path('htmx-form/', views.htmx_form, name='htmx_form'),
]
