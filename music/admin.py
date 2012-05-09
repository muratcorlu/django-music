from django.contrib import admin
from models import Song

class SongAdmin(admin.ModelAdmin):

    class Media:
        js = ('js/django-music/admin.js',)

admin.site.register(Song, SongAdmin)
