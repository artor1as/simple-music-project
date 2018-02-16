from django.urls import path

from remake_music.api_client import views as api_views


urlpatterns = [
    path('track/', api_views.TrackAPIList.as_view()),
    path('track/<int:pk>/', api_views.TrackAPIDetail.as_view()),
    path('like/', api_views.LikeAPIList.as_view()),
    path('like/<int:pk>/', api_views.LikeAPIDetail.as_view()),
    path('signup/', api_views.UserAPISignup.as_view())
]
