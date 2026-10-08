from rest_framework import serializers

from centers.serializers import CenterSerializer
from centers.models import CenterUser
from .models import User, USER_ROLE_CHOICES


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'role']

class LoginResponseSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=255, read_only=True)
    user = UserSerializer(read_only=True)
    center = serializers.SerializerMethodField()

    class Meta:
        fields = "__all__"
    
    def get_center(self, obj) -> CenterSerializer:
        if obj.get('user').role == USER_ROLE_CHOICES.USER:
            try:
                center_user = CenterUser.objects.get(user=obj.get('user'))
                return CenterSerializer(center_user.center).data
            except CenterUser.DoesNotExist:
                return None
        return None

class UserInformationSerializer(serializers.Serializer):
    user = UserSerializer(read_only=True)
    center = serializers.SerializerMethodField()
    
    def get_center(self, obj) -> CenterSerializer:
        if obj.get('user').role == USER_ROLE_CHOICES.USER:
            try:
                center_user = CenterUser.objects.get(user=obj.get('user'))
                return CenterSerializer(center_user.center).data
            except CenterUser.DoesNotExist:
                return None
        return None
