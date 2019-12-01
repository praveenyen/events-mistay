from django.conf.urls import url, include
from django.contrib import admin

from .views import MyEventsAPIView, InvitationAPIView, RegisteredAPIView, \
    InvitationDetailsView, EventCreateAPIView, RegisterForEventAPIView,\
    UserRegistration, PublicEventsAPIView

urlpatterns = [
    url(r'^events/public/$', PublicEventsAPIView.as_view()),
    url(r'^my/events/$', MyEventsAPIView.as_view()),
    url(r'^user/register', UserRegistration.as_view()),
    url(r'^events/register/$', RegisterForEventAPIView.as_view()),
    url(r'^events/create/$', EventCreateAPIView.as_view()),
    url(r'invitations/(?P<pk>.*)/$', InvitationDetailsView.as_view()),
    url(r'^invitations/$', InvitationAPIView.as_view()),
    url(r'^registered$', RegisteredAPIView.as_view())
]
