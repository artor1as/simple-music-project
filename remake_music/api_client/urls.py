from django.urls import path, include
from rest_framework.routers import DefaultRouter

from remake_music.api_client import views as api_views

router = DefaultRouter()
router.register(r'tracks', api_views.TrackViewSet)
router.register(r'artists', api_views.ArtistViewSet)
router.register(r'albums', api_views.AlbumViewSet)
router.register(r'likes', api_views.LikeViewSet)
router.register(r'users', api_views.UserViewSet)
router.register(r'', api_views.UserSignupViewSet)

urlpatterns = [
    # path('signup/', api_views.UserAPISignup.as_view()),
    path('', include(router.urls))
]
# TODO: Create read only router for authorized users
