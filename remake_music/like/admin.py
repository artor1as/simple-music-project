from django.contrib import admin

from remake_music.like.models import Like


class LikeAdmin(admin.ModelAdmin):
    readonly_fields = ('user', 'track')


admin.site.register(Like, LikeAdmin)
