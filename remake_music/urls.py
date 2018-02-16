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
from django.urls import path, include
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns

from remake_music.album import views as album_views
from remake_music.artist import views as artist_views
from remake_music.country import views as country_views
from remake_music.discovery import views as discovery_views
from remake_music.like import views as like_views
from remake_music.track import views as track_views
from remake_music.api_client import urls as api_urls


crud_patterns = [
    path('albums/', album_views.AlbumList.as_view()),
    path('albums/<int:pk>/', album_views.AlbumDetail.as_view()),
    path('artists/', artist_views.ArtistList.as_view()),
    path('artists/<int:pk>/', artist_views.ArtistDetail.as_view()),
    path('countries/', country_views.CountryList.as_view()),
    path('countries/<int:pk>/', country_views.CountryList.as_view()),
    path('discovery/', discovery_views.DiscoveryList.as_view()),
    path('discovery/<int:pk>/',
         discovery_views.DiscoveryDetail.as_view()),
    path('like/', like_views.LikeList.as_view()),
    path('like/<int:pk>/', like_views.LikeDetail.as_view()),
    path('tracks/', track_views.TrackList.as_view()),
    path('tracks/<int:pk>/', track_views.TrackDetail.as_view()),
]


version_patterns = [

]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_urls)),
    path('api-auth/', include('rest_framework.urls')),
]

urlpatterns = format_suffix_patterns(urlpatterns)

if settings.CRUD_MODE:
    urlpatterns = [
        path('crud/', include(crud_patterns)),
    ] + urlpatterns

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
