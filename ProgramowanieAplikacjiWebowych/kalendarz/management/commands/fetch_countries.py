import requests
from django.core.management.base import BaseCommand
from ...models import Country
from dotenv import load_dotenv
import os
load_dotenv()

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        API_KEY = os.environ.get('API_KEY')
        BASE_URL = 'https://holidayapi.com/v1/countries'
        params = {
            "key": API_KEY, 
        }

        response = requests.get(BASE_URL, params=params)

        if response.status_code == 200:
            countries = response.json().get("countries", [])
            if countries:
                for country in countries:
                    country_name = country.get("name")
                    country_code = country.get("code")
                    country_language = country.get("languages")
                    if len(country_language) == 0:
                        country_language = "en"
                    else:
                        country_language = country_language[0]
                    country_obj, created = Country.objects.get_or_create(
                        country=country_name, 
                        code=country_code,
                        language=country_language
                    )

                print(f"{len(countries)} countries added/updated in the database.")
        else:
            print(f"Error: {response.status_code} - {response.text}")