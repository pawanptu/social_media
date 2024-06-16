from django.urls import path
from .views import DiscussionListCreateView, DiscussionDetailView, DiscussionSearchView, DiscussionByHashtagView

urlpatterns = [
    path('', DiscussionListCreateView.as_view(), name='discussion-list-create'),
    path('<int:pk>/', DiscussionDetailView.as_view(), name='discussion-detail'),
    path('search/', DiscussionSearchView.as_view(), name='discussion-search'),
    path('tags/', DiscussionByHashtagView.as_view(), name='discussion-by-tag'),
]
