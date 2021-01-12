from django.contrib import auth
from .models import Usermodel
from rest_framework.decorators import permission_classes



from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import RegistrationSerializer

@permission_classes([AllowAny, ])
class RegistrationAPIView(APIView):
    serializer_class = RegistrationSerializer

    def post(self, request):
        serializer = RegistrationSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@permission_classes([AllowAny, ])
class LoginView(APIView):

    def post(self,request):
        try:
            data = request.data
            email = data.get('email','')
            password = data.get('password','')
            user = auth.authenticate(email=email,password = password)

            if user:
                auth_token = Usermodel._generate_jwt_token(user)

                serializer = RegistrationSerializer(user)

                data = {
                    'user':serializer.data,
                    'token':auth_token
                }
                return Response(data, status=status.HTTP_200_OK)
            return Response({'detail':'Invalid Credentials'},status = status.HTTP_401_UNAUTHORIZED)
        except KeyError:
            res = {'error': 'please provide a email and a password'}
            return Response(res)
