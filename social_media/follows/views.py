from rest_framework import generics, permissions
from .models import Follow
from .serializers import FollowSerializer
from rest_framework.permissions import IsAuthenticated

class FollowListCreateView(generics.ListCreateAPIView):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticated]

class FollowDetailView(generics.RetrieveDestroyAPIView):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticated]
