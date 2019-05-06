from django.core.management.base import BaseCommand
from ...models import User


class Command(BaseCommand):
    help = 'Create Users'

    def add_arguments(self, parser):
        parser.add_argument('-u', '--username', type=str, help='a username')
        parser.add_argument('-e', '--email', type=str, help='email address')
        parser.add_argument('-p', '--password', type=str, help='a password')
        parser.add_argument('-a', '--admin', action='store_true', help='create a staff user')
        parser.add_argument('-s', '--superuser', action='store_true', help='create a su user')

    def handle(self, *args, **kwargs):
        username = kwargs['username']
        email = kwargs['email']
        password = kwargs['password']
        is_staff = True if kwargs['admin'] else False
        is_superuser = True if kwargs['superuser'] else False
        User.objects.create_user(email=email, password=password, username=username,
                                 is_staff=is_staff, is_superuser=is_superuser
                                 )
