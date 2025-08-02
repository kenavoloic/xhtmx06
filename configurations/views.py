from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


def index(request):
    """Vue d'accueil publique (page de connexion)"""
    if request.user.is_authenticated:
        # Si l'utilisateur est déjà connecté, rediriger vers l'accueil
        from django.shortcuts import redirect
        return redirect('/accueil/')
    
    context = {
        'app_name': 'configurations',
        'project_name': 'xhtmx06',
    }
    return render(request, 'configurations/pages/index.html', context)


#@login_required
def accueil(request):
    """Vue d'accueil pour utilisateurs connectés"""
    context = {
        'user': request.user,
        'app_name': 'configurations',
        'project_name': 'xhtmx06',
    }
    return render(request, 'configurations/pages/accueil.html', context)


#@login_required
def htmx_example(request):
    """Exemple d'utilisation de HTMX"""
    if request.htmx:
        return HttpResponse("<p><strong>✅ Succès!</strong> Ceci a été chargé via HTMX!</p>")
    return render(request, 'configurations/pages/htmx_example.html')


#@login_required
def htmx_form(request):
    """Exemple de formulaire HTMX"""
    if request.method == 'POST' and request.htmx:
        name = request.POST.get('name', '')
        if name:
            return HttpResponse(f"<p class='alert alert-success'>Bonjour <strong>{name}</strong>! Formulaire soumis avec HTMX 🎉</p>")
        else:
            return HttpResponse("<p class='alert alert-danger'>Le nom est requis!</p>")
    
    return HttpResponse("<p>Méthode non autorisée</p>")
# Create your views here.
