from django.contrib import admin

# Register your models here.

from . models import photo, artista, adreess

admin.site.register(photo)
admin.site.register(artista)
admin.site.register(adreess)

