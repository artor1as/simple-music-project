from django.contrib import admin

from remake_music.album.models import Album
from remake_music.track.models import Track


class TrackInLine(admin.TabularInline):
    model = Track
    extra = 0


class AlbumAdmin(admin.ModelAdmin):
    inlines = [TrackInLine]


admin.site.register(Album, AlbumAdmin)
