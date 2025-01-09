from django.core.management.base import BaseCommand
from ...models import User

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('login', type=str)
        parser.add_argument('password', type=str)

    def handle(self, *args, **kwargs):
        login = kwargs['login']
        pass_word= kwargs['password']


        if User.objects.filter(username=login).exists() or User.objects.filter(email=login).exists():
            if User.objects.filter(password=pass_word).exists():
                print("Loged in")
            else:
                print("Incorect login or password")
        else:
            print("Incorect login or password")