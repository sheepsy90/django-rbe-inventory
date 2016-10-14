from django.contrib.auth.models import User
from django.db import models


class InvitationKey(models.Model):
    user = models.ForeignKey(User)
    key = models.CharField(max_length=64, unique=True, help_text="The unique key for invite identification!")
    email = models.EmailField(max_length=128, default='', help_text="The email to send the invite too!")

    class Meta:
        unique_together = [('user', 'email')]
        db_table = 'invitation_key'


class UserProfile(models.Model):
    user = models.OneToOneField(User, null=True, default=None, related_name='user')
    invited_by = models.ForeignKey(User, related_name='invited_by', null=True)
    about_me_text = models.TextField(max_length=3000, default='')
    avatar_link = models.URLField(blank=True)