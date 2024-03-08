from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Video


class VideoListView(ListView):
    model = Video
    template_name = 'videos/video_list.html'
    context_object_name = 'videos'


class VideoDetailView(DetailView):
    model = Video
    template_name = 'videos/video_detail.html'
    context_object_name = 'video'


class VideoSearchView(ListView):
    model = Video
    template_name = 'videos/video_search.html'
    context_object_name = 'videos'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Video.objects.filter(title__icontains=query)
        return Video.objects.all()
