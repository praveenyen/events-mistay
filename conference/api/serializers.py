from rest_framework import serializers
from ..models import *


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = [
            'event_name',
            'starts_on',
            'ends_on',
            'users_limit',
            'is_public'
        ]


class InvitationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invitation
        fields = [
            'event',
            'user',
            'created_at'
        ]


class RegisteredSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegisterEvent
        fields = [
            'user',
            'event',
            'created_at'
        ]
