from rest_framework import serializers
from ..models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password'
        ]


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = [
            'id',
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


class RegisteredEventsSerializer(serializers.ModelSerializer):
    event = EventSerializer(read_only=True)

    class Meta:
        model = RegisterEvent
        fields = [
            'user',
            'event',
            'created_at'
        ]
