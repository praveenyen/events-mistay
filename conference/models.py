from django.db import models
from django.contrib.auth.models import User, AbstractUser


# Create your models here
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
    event = models.ForeignKey(Event, related_name="event_invitations", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="event_invitations", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        print(self.event)
        return '{} || {}'.format(self.event.event_name, self.user.username)
