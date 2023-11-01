from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .serializers import CustomUserSerializer
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework import status

class CustomUserCreate(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = CustomUserSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        user = get_user_model().objects.get(id=response.data['id'])
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'user_id': response.data['id']})

class LoginView(APIView):

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)

        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({"token": token.key})
        else:
            return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)
        
class LogoutView(APIView):
    def post(self, request):
        # simply delete the token to force a login
        request.auth.delete()
        return Response(status=status.HTTP_200_OK)