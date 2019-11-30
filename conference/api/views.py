from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication
from rest_framework.response import Response
from rest_framework import generics, permissions

from ..models import Event, Invitation, RegisterEvent
from .serializers import EventSerializer, InvitationSerializer, RegisteredSerializer


class EventAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [SessionAuthentication]

    def get(self, request, format=None):
        req_user_id = self.request.user.id

        qs = Event.objects.filter(user__id=req_user_id)
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
