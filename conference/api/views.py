from django.contrib.auth.models import User
from django.db import IntegrityError
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication
from rest_framework.response import Response
from rest_framework import generics, permissions
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from ..models import Event, Invitation, RegisterEvent
from .serializers import EventSerializer, InvitationSerializer, \
    RegisteredSerializer, UserSerializer, RegisteredEventsSerializer


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


class InvitedEventsAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JSONWebTokenAuthentication]

    def get(self, request, format=None):
        req_user_id = self.request.user.id

        qs = Event.objects.filter(event_invitations__user_id=req_user_id)
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
    authentication_classes = [JSONWebTokenAuthentication]

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


class EventDeleteAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JSONWebTokenAuthentication]

    def post(self, request, format=None):
        user_id = self.request.user.id
        request_data = self.request.data

        try:
            event_id = request_data['event_id']

            if is_not_a_owner_of_the_event(
                    event_id=event_id, user_id=user_id):
                response = {
                    "details": "Only Event Owner Can Delete."
                }
                return Response(response, status=400)

            Event.objects.get(id=event_id).delete()

            return Response(
                {"details": "Successfully Deleted"}, status=200
            )

        except KeyError:
            response = {
                "details": "You should provide all"
                           " sufficient information to register"
            }
            return Response(response, status=400)


class RegisterForEventAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JSONWebTokenAuthentication]

    def post(self, request, format=None):
        user_id = self.request.user.id
        request_data = self.request.data

        try:
            event_id = request_data['event_id']
            event = Event.objects.get(id=event_id)

            if self.is_seats_not_available(event):
                response = {
                    "details": "All seats are occupied, Try Next event."
                }
                return Response(response, status=400)

            is_overlapping = self.is_overlapping(
                user_id=user_id, event=event)
            if is_overlapping:
                response = {
                    "details": "This event is overlapping "
                               "with your registered events."
                }
                return Response(response, status=400)
        except KeyError:
            response = {
                "details": "You should provide all"
                           " sufficient information to register"
            }
            return Response(response, status=400)

        qs = RegisterEvent.objects.create(
            user_id=user_id, event_id=event_id
        )

        serializer = RegisteredSerializer(qs)
        return Response(serializer.data)

    @staticmethod
    def is_seats_not_available(event):
        registered_users_count = RegisterEvent.objects.filter(
            event=event).count()
        if registered_users_count < event.users_limit:
            return False
        return True

    @staticmethod
    def is_overlapping(user_id, event):
        not_overlapping_count = RegisterEvent.objects.filter(
            Q(event__starts_on__gte=event.starts_on) | Q(
                event__ends_on__lt=event.ends_on),
            user_id=user_id
        ).count()
        all_registered_events_count = RegisterEvent.objects.filter(
            user_id=user_id).count()

        if all_registered_events_count == 0:
            return False
        if not_overlapping_count == all_registered_events_count:
            return True
        return False


class InviteForEventAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JSONWebTokenAuthentication]

    def post(self, request, format=None):
        user_id = self.request.user.id
        request_data = self.request.data

        try:
            event_id = request_data['event_id']

            if is_not_a_owner_of_the_event(
                    event_id=event_id, user_id=user_id):
                response = {
                    "details": "Only Event Owner Can Send Invitation."
                }
                return Response(response, status=400)

            Invitation.objects.get_or_create(event_id=event_id, user_id=user_id)

            return Response(
                {"details": "Successfully Invited"}, status=200
            )

        except KeyError:
            response = {
                "details": "You should provide all"
                           " sufficient information to register"
            }
            return Response(response, status=400)


def is_not_a_owner_of_the_event(event_id, user_id):
    is_not_owner = not Event.objects.filter(
        id=event_id, user_id=user_id).exists()

    return is_not_owner


class RegisteredEventsAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JSONWebTokenAuthentication]

    def get(self, request, format=None):
        req_user_id = self.request.user.id

        qs = RegisterEvent.objects.filter(user_id=req_user_id).select_related(
            'event'
        )

        serializer = RegisteredEventsSerializer(qs, many=True)

        return Response(serializer.data)


class UnRegisterForEventAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JSONWebTokenAuthentication]

    def post(self, request, format=None):
        user_id = self.request.user.id
        request_data = self.request.data

        try:
            event_id = request_data['event_id']
        except KeyError:
            response = {
                "details": "You should provide all"
                           " sufficient information to register"
            }
            return Response(response, status=400)
        try:
            RegisterEvent.objects.get(
                event_id=event_id, user_id=user_id).delete()
        except:
            response = {
                "details": "You have already un-registered for the event."
            }
            return Response(response, status=404)

        response = {
            "details": "You have un-registered for the event."
        }
        return Response(response, status=200)


class InvitationAPIView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JSONWebTokenAuthentication]
    serializer_class = InvitationSerializer

    def get_queryset(self):
        req_user_id = self.request.user.id
        qs = Invitation.objects.filter(user__id=req_user_id)
        query = self.request.GET.get('q')

        if query is not None:
            qs = qs.filter(event__event_name__icontains=query)
        return qs
