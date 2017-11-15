"""remake_music URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns

from album import views as album_views
from artist import views as artist_views
from country import views as country_views
from discovery import views as discovery_views
from like import views as like_views
from track import views as track_views


crud_patterns = [
    url(r'^albums/$', album_views.AlbumList.as_view()),
    url(r'^albums/(?P<pk>[0-9]+)/$', album_views.AlbumDetail.as_view()),
    url(r'^artists/$', artist_views.ArtistList.as_view()),
    url(r'^artists/(?P<pk>[0-9]+)/$', artist_views.ArtistDetail.as_view()),
    url(r'^countries/$', country_views.CountryList.as_view()),
    url(r'^countries/(?P<pk>[0-9]+)/$', country_views.CountryList.as_view()),
    url(r'^discovery/$', discovery_views.DiscoveryList.as_view()),
    url(r'^discovery/(?P<pk>[0-9]+)/$',
        discovery_views.DiscoveryDetail.as_view()),
    url(r'^like/$', like_views.LikeList.as_view()),
    url(r'^like/(?P<pk>[0-9]+)/$', like_views.LikeDetail.as_view()),
    url(r'^tracks/$', track_views.TrackList.as_view()),
    url(r'^tracks/(?P<pk>[0-9]+)/$', track_views.TrackDetail.as_view()),
    url(r'^api-auth/', include('rest_framework.urls')),
]

version_patterns = [

]

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^crud/', include(crud_patterns)),
]

urlpatterns = format_suffix_patterns(urlpatterns)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
