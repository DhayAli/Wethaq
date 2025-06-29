from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from helpers.utils import swagger_response
from .serializers import LoginResponseSerializer, UserInformationSerializer


class LoginView(APIView):
    """Endpoint to login a user and return user details"""

    permission_classes = (AllowAny, )
    serializer_class = AuthTokenSerializer
    
    
    @swagger_response(response_schema={
        200:LoginResponseSerializer,
        400: {
            "non_field_errors" : ["Unable to log in with provided credentials."]
        },
        401: None,
        404: None,
    })
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, _ = Token.objects.get_or_create(user=user)
        
        # Add user's center if he has (user can only be in one center)
        response_data = LoginResponseSerializer({
            'token': token.key,
            'user': user
        })
        
        return Response(response_data.data, status=status.HTTP_200_OK)


class UserInformationView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserInformationSerializer
    
    @swagger_response(response_schema={
        200:UserInformationSerializer,
        400: None,
        404: None,
    })
    def get(self, request, *args, **kwargs):
        user = request.user
        
        data = UserInformationSerializer({"user": user}).data
        
        return Response(data, status=status.HTTP_200_OK)
