from django.contrib import admin

from remake_music.track.models import *


class TrackAdmin(admin.ModelAdmin):
    list_display = ('name', 'album', 'path')


admin.site.register(Track, TrackAdmin)
