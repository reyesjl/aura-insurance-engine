# filepath: aura_backend/core/auth_views.py
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from django.db.models import Q
from .serializers import UserSerializer

User = get_user_model()

@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    """
    Login endpoint that returns JWT tokens
    Accepts both email and username for login
    """
    login_field = request.data.get('email') or request.data.get('username') or request.data.get('loginField')
    password = request.data.get('password')
    
    if not login_field or not password:
        return Response({
            'error': 'Email/username and password are required'
        }, status=status.HTTP_400_BAD_REQUEST)
    
    # Try to find user by email OR username
    try:
        user = User.objects.get(
            Q(email=login_field.lower()) | Q(username=login_field.lower())
        )
    except User.DoesNotExist:
        return Response({
            'error': 'Invalid credentials. Does not exist.'
        }, status=status.HTTP_401_UNAUTHORIZED)
    
    # Authenticate user (Django's authenticate expects username)
    authenticated_user = authenticate(username=user.username, password=password)
    if not authenticated_user:
        return Response({
            'error': 'Invalid credentials. Please check your username/email and password.'
        }, status=status.HTTP_401_UNAUTHORIZED)
    
    # Generate tokens
    refresh = RefreshToken.for_user(authenticated_user)
    access = refresh.access_token
    
    # Serialize user data
    user_serializer = UserSerializer(authenticated_user)
    
    return Response({
        'access': str(access),
        'refresh': str(refresh),
        'user': user_serializer.data
    }, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([AllowAny])
def register_view(request):
    """
    Register endpoint that creates user and returns JWT tokens
    """
    email = request.data.get('email')
    username = request.data.get('username')
    password = request.data.get('password')
    confirm_password = request.data.get('confirmPassword')
    
    if not email or not password or not confirm_password or not username:
        return Response({
            'error': 'Email, username, password, and confirm password are required'
        }, status=status.HTTP_400_BAD_REQUEST)
    
    if password != confirm_password:
        return Response({
            'error': 'Passwords do not match'
        }, status=status.HTTP_400_BAD_REQUEST)
    
    # Check if user already exists by email
    if User.objects.filter(email=email.lower()).exists():
        return Response({
            'error': 'User with this email already exists'
        }, status=status.HTTP_400_BAD_REQUEST)
    
    # Determine username - use provided username or fall back to email
    final_username = username.lower() if username else email.lower()
    
    # Check if username already exists
    if User.objects.filter(username=final_username).exists():
        return Response({
            'error': 'Username already exists'
        }, status=status.HTTP_400_BAD_REQUEST)
    
    # Create user
    try:
        user = User.objects.create_user(
            username=final_username,
            email=email.lower(),
            password=password,
            is_agent=False,
            agent_name=f"Agent {email.split('@')[0].title()}" # Default agent name based on email prefix
        )
        
        # Generate tokens
        refresh = RefreshToken.for_user(user)
        access = refresh.access_token
        
        # Serialize user data
        user_serializer = UserSerializer(user)
        
        return Response({
            'access': str(access),
            'refresh': str(refresh),
            'user': user_serializer.data
        }, status=status.HTTP_201_CREATED)
        
    except Exception as e:
        return Response({
            'error': f'Registration failed: {str(e)}'
        }, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def logout_view(request):
    """
    Logout endpoint that blacklists the refresh token
    """
    try:
        refresh_token = request.data.get('refresh')
        if refresh_token:
            token = RefreshToken(refresh_token)
            token.blacklist()
        return Response({'message': 'Successfully logged out'}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def user_profile_view(request):
    """
    Get current user profile (requires authentication)
    """
    serializer = UserSerializer(request.user)
    return Response(serializer.data)