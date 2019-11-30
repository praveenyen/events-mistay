from django.contrib.auth.models import User
from django.db import IntegrityError
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication
from rest_framework.response import Response
from rest_framework import generics, permissions
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from ..models import Event, Invitation, RegisterEvent
from .serializers import EventSerializer, InvitationSerializer, \
    RegisteredSerializer, UserSerializer


class UserRegistration(APIView):
    permission_classes = []
    authentication_classes = []

    def post(self, request, format=None):
        request_data = self.request.data

        first_name = request_data['first_name']
        last_name = request_data['last_name']
        email = request_data['email']
        username = request_data['username']
        password = request_data['password']

        try:
            qs = User.objects.create(
                first_name=first_name, last_name=last_name, email=email,
                username=username
            )
            qs.set_password(raw_password=password)
            qs.save()
        except IntegrityError:
            response = {
                "details": "Username Already Taken"
            }
            return Response(response, status=400)

        serializer = UserSerializer(qs)
        return Response(serializer.data)


class MyEventsAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JSONWebTokenAuthentication]

    def get(self, request, format=None):
        req_user_id = self.request.user.id

        qs = Event.objects.filter(user__id=req_user_id)
        serializer = EventSerializer(qs, many=True)

        return Response(serializer.data)


class PublicEventsAPIView(APIView):
    permission_classes = []
    authentication_classes = []

    def get(self, request, format=None):
        req_user_id = self.request.user.id

        qs = Event.objects.filter(is_public=True)
        serializer = EventSerializer(qs, many=True)

        return Response(serializer.data)


class EventCreateAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [SessionAuthentication]

    def post(self, request, format=None):
        user_id = self.request.user.id
        request_data = self.request.data

        event_name = request_data['event_name']
        starts_on = request_data['starts_on']
        ends_on = request_data['ends_on']
        is_public = request_data['is_public']
        users_limit = request_data['users_limit']

        qs = Event.objects.create(
            user_id=user_id, event_name=event_name, starts_on=starts_on,
            ends_on=ends_on, is_public=is_public, users_limit=users_limit
        )

        serializer = EventSerializer(qs)
        return Response(serializer.data)


class RegisterEventAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [SessionAuthentication]

    def post(self, request, format=None):
        user_id = self.request.user.id
        request_data = self.request.data

        event_id = request_data['event_id']

        qs = RegisterEvent.objects.create(
            user_id=user_id, event_id=event_id
        )

        serializer = RegisteredSerializer(qs)
        return Response(serializer.data)


class InvitationAPIView(generics.ListAPIView):
    permission_classes = []
    authentication_classes = [SessionAuthentication]
    serializer_class = InvitationSerializer

    def get_queryset(self):
        req_user_id = self.request.user.id
        qs = Invitation.objects.filter(user__id=req_user_id)
        query = self.request.GET.get('q')

        if query is not None:
            qs = qs.filter(event__event_name__icontains=query)
        return qs


class InvitationDetailsView(generics.RetrieveAPIView):
    permission_classes = []
    authentication_classes = []
    queryset = Invitation.objects.all()
    serializer_class = InvitationSerializer

    def get_object(self):
        kwargs = self.kwargs
        kw_id = kwargs.get('pk')
        return Invitation.objects.get(id=kw_id.split('/')[1])


class RegisteredAPIView(generics.ListAPIView):
    permission_classes = []
    authentication_classes = []
    queryset = RegisterEvent.objects.all()
    serializer_class = RegisteredSerializer
