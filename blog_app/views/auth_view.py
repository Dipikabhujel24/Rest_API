from rest_framework.decorators import api_view
from rest_framework_simplejwt.tokens import RefreshToken
#from rest_framework import permissions
#from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status


#Function to generate token
def get_token_for_user(user):
    refresh = RefreshToken.for_user(user)
    return{
        'refresh': str(refresh),
        'access': str(refresh.access_token)
    }

@api_view(['POST'])
#@permissions([IsAuthenticated])
def register_user(request):
    username = request.data.get('username')
    password = request.data.get('password')
    email = request.data.get('email')

    if User.objects.filter(username=username).exists():
        return Response({'err':"Username already exists."})
    try:
        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        return Response({'msg':'User Registered Successfully'},status=status.HTTP_200_OK)
    except:
        return Response({'err':"Failed To Register"},status=status.HTTP_400_BAD_REQUEST)


