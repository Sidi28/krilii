from __future__ import unicode_literals
from django.db import models

from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible

# Create your models here.
class produit(models.Model):
    image=models.ImageField(upload_to="photo/")
    titre=models.CharField(max_length=30)
    prix=models.IntegerField()
    telephone=models.IntegerField(default=0)
    imgcuisine=models.ImageField(upload_to="photo/",default='DEFAULT')
    infocuisine=models.TextField(null=True)
    imgchambre=models.ImageField(upload_to="photo/",default='DEFAULT')
    infochambre=models.TextField(null=True)
    imgdouche=models.ImageField(upload_to="photo/",default='DEFAULT')
    infodouche=models.TextField(null=True)
   
    categ=models.ForeignKey('Categorie', on_delete=models.PROTECT)
    
    def __str__(self):
       return  self.titre
    
class Categorie(models.Model):
	nom=models.CharField(max_length=70)
	
	def __str__(self):
	      return  "{0}".format(self.nom)
 