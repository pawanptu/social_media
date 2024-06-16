from django.urls import path
from .views import FollowListCreateView, FollowDetailView

urlpatterns = [
    path('', FollowListCreateView.as_view(), name='follow-list-create'),
    path('<int:pk>/', FollowDetailView.as_view(), name='follow-detail'),
]
