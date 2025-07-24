from rest_framework.decorators import api_view, permission_classes
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate


#Function to generate token
def get_token_for_user(user):
    refresh = RefreshToken.for_user(user)
    return{
        'refresh': str(refresh),
        'access': str(refresh.access_token)
    }

@api_view(['POST'])
@permission_classes([AllowAny])
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

@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if not username:
       return Response({'err':'Username is required.'},status=status.HTTP_400_BAD_REQUEST)
    elif not User.objects.filter(username=username).exists():
        return Response({'err':'Invalid username.'},status=status.HTTP_400_BAD_REQUEST)
    
    if not password:
       return Response({'err':'Password is required.'},status=status.HTTP_400_BAD_REQUEST)

    user = authenticate(username=username, password=password)
    if user is not None:
        tokens = get_token_for_user(user)
        return Response({
            'msg':'User Login Successful.',
            'tokens': tokens},status=status.HTTP_200_OK)
    else:
        return Response({'err':'Incorrect Password'},status=status.HTTP_204_NO_CONTENT)