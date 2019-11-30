from django.conf.urls import url, include
from django.contrib import admin

from .views import EventAPIView, InvitationAPIView, RegisteredAPIView,\
    InvitationDetailsView, EventCreateAPIView, RegisterEventAPIView

urlpatterns = [
    url(r'^events/$', EventAPIView.as_view()),
    url(r'^events/register/$', RegisterEventAPIView.as_view()),
    url(r'^events/create/$', EventCreateAPIView.as_view()),
    url(r'invitations/(?P<pk>.*)/$', InvitationDetailsView.as_view()),
    url(r'^invitations/$', InvitationAPIView.as_view()),
    url(r'^registered$', RegisteredAPIView.as_view())
]
