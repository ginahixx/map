from django.contrib import admin

# Register your models here.
from .models import Site, Block, Parcel

admin.site.register(Site)
admin.site.register(Block)
admin.site.register(Parcel)

#superuser
#gina, hixxjunk@gmail.com, ginahixx
