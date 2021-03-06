from django.conf.urls import url, include
from django.contrib import admin

from .views import MyEventsAPIView, InvitationAPIView, \
    EventCreateAPIView, RegisterForEventAPIView, \
    UserRegistration, PublicEventsAPIView, RegisteredEventsAPIView, \
    UnRegisterForEventAPIView, InviteForEventAPIView, EventDeleteAPIView, \
    InvitedEventsAPIView

urlpatterns = [
    url(r'^events/$', MyEventsAPIView.as_view()),
    url(r'^events/create/$', EventCreateAPIView.as_view()),
    url(r'^events/delete/$', EventDeleteAPIView.as_view()),
    url(r'^events/public/$', PublicEventsAPIView.as_view()),
    url(r'^events/invited/$', InvitedEventsAPIView.as_view()),
    url(r'^events/register/$', RegisterForEventAPIView.as_view()),
    url(r'^events/invite/$', InviteForEventAPIView.as_view()),
    url(r'^events/un-register/$', UnRegisterForEventAPIView.as_view()),
    url(r'^events/registered/$', RegisteredEventsAPIView.as_view()),

    url(r'^user/register', UserRegistration.as_view())
]
