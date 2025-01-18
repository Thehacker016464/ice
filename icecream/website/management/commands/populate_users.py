from website.models import user
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Populate users'

    def handle(self, *args, **kwargs):
        name = [
            'John Doe',
            'Jane Doe',
            'Alice Doe',
            'Bob Doe',
            'Emily Doe',
        ]
        email = [
            'John Doe',
            'Jane Doe',
            'Alice Doe',
            're told to'
            'Emily Doe',
        ]
        password = [
            'password',
            'password',
            'password',
            'password',
            'password',
        ]
        for name,email,password in zip(name,email,password):
            user.objects.create(name=name,email=email,password=password)
        self.stdout.write(self.style.SUCCESS('Successfully created user'))