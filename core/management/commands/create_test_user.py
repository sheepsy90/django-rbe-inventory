from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from profile.models import UserProfile


class Command(BaseCommand):
    help = 'Creates a user for testing the system'

    def handle(self, *args, **options):
        User.objects.filter(username='sheepy').delete()
        u = User.objects.create_superuser('sheepy', 'sheepy@test.de', 'aqwsderf')
        p = UserProfile(user=u, invited_by=None, is_confirmed=True)
        p.save()

        self.stdout.write(self.style.SUCCESS('Successfully create test user!'))