from django.contrib import admin

from album.models import Album
from track.models import Track


class TrackInLine(admin.TabularInline):
    model = Track
    extra = 0


class AlbumAdmin(admin.ModelAdmin):
    inlines = [TrackInLine]


admin.site.register(Album, AlbumAdmin)
