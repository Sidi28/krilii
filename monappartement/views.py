from django.shortcuts import render,redirect
from django.http import HttpResponse
from monappartement.models import produit,Categorie
# Create your views here.

def voir_produit(request):
    produits=produit.objects.all()
    return render(request,"monappartement/index.html",locals())

def voir_details(request,id):
    try:
        produits=produit.objects.get(id=id)
    except DoesNotExist:
        raise Http404
    return render(request,"monappartement/details.html",{'produits': produits})
    

