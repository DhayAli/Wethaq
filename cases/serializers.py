from rest_framework import serializers

from .models import Case, Detainee, Notification
from centers.serializers import CenterSerializer

class DetaineeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detainee
        fields = '__all__'

class CreateCaseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Case
        fields = ['id', 'detainee', 'center', 'charge', 'case_number', 'arresting_authority', 'arresting_place', 'arresting_date', 'detention_agency']

class CaseSerializer(serializers.ModelSerializer):
    detainee = DetaineeSerializer(read_only=True)
    center = CenterSerializer(read_only=True)

    class Meta:
        model = Case
        fields = '__all__'


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'