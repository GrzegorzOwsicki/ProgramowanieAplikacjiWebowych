from django.core.management.base import BaseCommand
from ...models import User, Country

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('username', type=str)
        parser.add_argument('email', type=str)
        parser.add_argument('password', type=str)
        parser.add_argument('country', type=str)
        
    def handle(self, *args, **kwargs):
        user_name = kwargs['username']
        mail = kwargs['email']
        pass_word= kwargs['password']
        countryy = kwargs['country']

        

        if not User.objects.filter(email=mail).exists():
            if not User.objects.filter(username=user_name).exists():
                user_username = user_name
                user_email = mail
                user_password = pass_word
                user_country = Country.objects.get(code = countryy)
        
                user_obj, created = User.objects.get_or_create(
                    username = user_username,
                    email = user_email, 
                    password = user_password,
                    country = user_country
                )
                print(user_obj.id)
            else:
                print("Username allerdy in use")
        else:
            print("Email allerdy in use")