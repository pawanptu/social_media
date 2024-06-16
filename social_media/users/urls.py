from django.urls import path
from .views import UserListCreateView, UserDetailView, UserSearchView, FollowUserView, LoginView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('', UserListCreateView.as_view(), name='user-list-create'),
    path('<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('search/', UserSearchView.as_view(), name='user-search'),
    path('<int:pk>/follow/', FollowUserView.as_view(), name='user-follow'),
]
