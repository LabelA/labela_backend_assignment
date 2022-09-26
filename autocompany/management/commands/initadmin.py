from django.contrib.auth.models import User
from django.core.management import BaseCommand

from autocompany import settings


class Command(BaseCommand):

    def handle(self, *args, **options):
        if User.objects.count() == 0:
            username = settings.ADMIN_USERNAME.replace(' ', '')
            email = settings.ADMIN_EMAIL
            password = settings.ADMIN_INITIAL_PASSWORD
            print('Creating admin account for %s (%s)' % (username, email))
            admin = User.objects.create_superuser(email=email, username=username, password=password)
            admin.has_usable_password()
            admin.is_active = True
            admin.is_admin = True
            admin.save()
        else:
            print('Admin accounts can only be initialized if no Accounts exist')
