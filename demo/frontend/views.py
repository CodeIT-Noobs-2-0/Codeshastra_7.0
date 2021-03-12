from django.shortcuts import render
from rest_framework import generics
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.models import Token
from .serializers import *

# Create your views here.

def index(request):
    return render(request, 'build/index.html')


class RegisterUser(generics.GenericAPIView):
    serializer_class = UserRegisterSerializer1

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        if user is not None:
            # A backend authenticated the credentials
            try:
                token = Token.objects.get(user=user.id)
            except Token.DoesNotExist:
                token = Token.objects.create(user=user)

        # print(token.key)

        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": token.key,
            # "token": AuthToken.objects.create(user)[1]
        })