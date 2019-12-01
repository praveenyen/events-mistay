from django.conf.urls import url, include
from django.contrib import admin

from .views import MyEventsAPIView, InvitationAPIView, RegisteredAPIView, \
    EventCreateAPIView, RegisterForEventAPIView, \
    UserRegistration, PublicEventsAPIView, RegisteredEventsAPIView, \
    UnRegisterForEventAPIView, InviteForEventAPIView, EventDeleteAPIView

urlpatterns = [
    url(r'^events/public/$', PublicEventsAPIView.as_view()),
    url(r'^events/$', MyEventsAPIView.as_view()),
    url(r'^user/register', UserRegistration.as_view()),
    url(r'^events/register/$', RegisterForEventAPIView.as_view()),
    url(r'^events/invite/$', InviteForEventAPIView.as_view()),
    url(r'^events/un-register/$', UnRegisterForEventAPIView.as_view()),
    url(r'^events/registered/$', RegisteredEventsAPIView.as_view()),
    url(r'^events/create/$', EventCreateAPIView.as_view()),
    url(r'^events/delete/$', EventDeleteAPIView.as_view()),
    # url(r'(?P<pk>.*)/$', InvitationDetailsView.as_view()),
    url(r'^invitations/$', InvitationAPIView.as_view()),
    url(r'^registered$', RegisteredAPIView.as_view())
]
