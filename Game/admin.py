from django.contrib import admin

from .models import (
    Counties, 
    Representatives,
    Parties,
    General,
    Topics,
    Deals
)

admin.site.register(Counties)
admin.site.register(Representatives)
admin.site.register(Parties)
admin.site.register(General)
admin.site.register(Topics)
admin.site.register(Deals)
