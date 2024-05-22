

from django.http import HttpResponse

# def home(request):
#     return HttpResponse("Hello, world. You're at the polls home page.")
    
from django.urls import reverse

def test(request):
    # Récupérer les noms d'URL principaux
    index_url = reverse('home')  # URL de la page d'accueil
    #owner_url = reverse('owner')  # URL de la page du propriétaire
    # Vous pouvez continuer ainsi pour les autres URLs principales

    # Créer une liste des URLs principales
    main_urls = [
        ('Accueil', index_url),
        #('Page du propriétaire', owner_url),
        # Ajoutez les autres URLs principales de la même manière
    ]

    # Créer une chaîne de caractères HTML pour afficher les liens
    links_html = '<ul>'
    for name, url in main_urls:
        links_html += f'<li><a href="{url}">{name}</a></li>'
    links_html += '</ul>'

    # Renvoyer une réponse HTTP contenant les liens
    return HttpResponse(f"Voici les principales URLs de votre site : {links_html}")


# mysite/views.py

from django.http import HttpResponse
from django.urls import reverse

def home(request):
    # Obtenez les URLs des vues de l'application "polls"
    index_url = reverse('home')  # URL de la page d'accueil
    polls_index_url = reverse('polls:index')
    #polls_owner_url = reverse('polls:owner')
    # Continuez avec d'autres URLs de l'application "polls" si nécessaire

    # Créez une liste des sous-liens de l'application "polls"
    polls_sublinks = [
        ('Accueil', index_url),
        ('Page d\'accueil des sondages', polls_index_url),
        #('Page du propriétaire', polls_owner_url),
        # Ajoutez d'autres sous-liens si nécessaire
    ]

    # Créez une chaîne HTML pour afficher les sous-liens de l'application "polls"
    polls_links_html = '<ul>'
    for name, url in polls_sublinks:
        polls_links_html += f'<li><a href="{url}">{name}</a></li>'
    polls_links_html += '</ul>'

    # Renvoyez une réponse HTTP contenant les sous-liens de l'application "polls"
    return HttpResponse(f"Voici les sous-liens de l'application \"polls\" : {polls_links_html}")
