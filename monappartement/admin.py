from django.contrib import admin
from monappartement.models import produit,Categorie

class produitAdmin(admin.ModelAdmin):
    list_display=('titre','image','prix')
    list_filter=('titre','categ',)
    search_fields=('titre',)
    
    fieldsets = (
      # Fieldset 1 : meta-info (titre, auteur?)
      ('General', {
                     'classes': ['collapse',],
                     'fields': ('titre', 'image', 'categ','telephone','prix','imgcuisine','infocuisine','imgchambre','infochambre','imgdouche','infodouche')
                  }
       ),
       )
# Register your models here.
admin.site.register(produit,produitAdmin)
admin.site.register(Categorie)

 
