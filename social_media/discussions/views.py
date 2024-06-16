from rest_framework import generics, permissions
from .models import Discussion, Hashtag
from .serializers import DiscussionSerializer
from rest_framework.permissions import IsAuthenticated

class DiscussionListCreateView(generics.ListCreateAPIView):
    queryset = Discussion.objects.all()
    serializer_class = DiscussionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class DiscussionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Discussion.objects.all()
    serializer_class = DiscussionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class DiscussionSearchView(generics.ListAPIView):
    serializer_class = DiscussionSerializer

    def get_queryset(self):
        text = self.request.query_params.get('text', None)
        return Discussion.objects.filter(text__icontains=text)

class DiscussionByHashtagView(generics.ListAPIView):
    serializer_class = DiscussionSerializer

    def get_queryset(self):
        tags = self.request.query_params.get('tags', None).split(',')
        return Discussion.objects.filter(hashtags__name__in=tags).distinct()
