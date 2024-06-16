from rest_framework import generics, permissions
from .models import User
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        
class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserSearchView(generics.ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        name = self.request.query_params.get('name', None)
        return User.objects.filter(username__icontains=name)

class FollowUserView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        user_to_follow = User.objects.get(pk=pk)
        request.user.following.add(user_to_follow)
        return Response({'status': 'followed'})

    def delete(self, request, pk):
        user_to_unfollow = User.objects.get(pk=pk)
        request.user.following.remove(user_to_unfollow)
        return Response({'status': 'unfollowed'})
