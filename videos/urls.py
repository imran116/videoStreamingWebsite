from django.urls import path
from videos.views import VideoListView, VideoDetailView, VideoSearchView

urlpatterns = [
    path('', VideoListView.as_view(), name='video_list'),
    path('video/<int:pk>/', VideoDetailView.as_view(), name='video_detail'),
    path('search/', VideoSearchView.as_view(), name='video_search'),
]
