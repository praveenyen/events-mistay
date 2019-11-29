from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Event(models.Model):
    user = models.ForeignKey(User, related_name="events", on_delete=None)
    event_name = models.CharField(max_length=200)
    starts_on = models.DateTimeField()
    ends_on = models.DateTimeField()
    is_public = models.BooleanField(default=True)
    users_limit = models.IntegerField(default=10)

    def __str__(self):
        return '{}'.format(self.event_name)


class RegisterEvent(models.Model):
    user = models.ForeignKey(User, related_name="registered_events", on_delete=None)
    event = models.ForeignKey(Event, related_name="registered", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class Invitation(models.Model):
    event = models.ManyToManyField(Event, related_name="event_invitations")
    user = models.ManyToManyField(User, related_name="event_invitations")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        print(self.event)
        return '{} || {}'.format(self.event, self.user)
