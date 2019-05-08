import os
from django.core.management.base import BaseCommand
from ...models import User


class Command(BaseCommand):
    help = 'Create Users on Heroku'

    def handle(self, *args, **kwargs):
        db= os.environ['DATABASE_URL']
        print(db)
        username = os.environ['username']

        email = os.environ['email']
        print(email)
        password = os.environ['password']
        is_staff = True

        if User.objects.all().filter(username=username).count() < 1:
            User.objects.create_user(email=email, password=password, username=username, is_staff=is_staff)
