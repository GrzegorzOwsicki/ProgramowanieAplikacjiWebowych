import requests
from datetime import datetime
from django.core.management.base import BaseCommand
from ...models import Holiday,Country
from dotenv import load_dotenv
import os

load_dotenv()

class Command(BaseCommand):

    def handle(self, *args, **kwargs):


        countries = Country.objects.values_list("code")
        n = 0
        countriesString = ""
        countriestab = []
        for i in countries:
            countriesString += i[0] + ","
            n+=1
            if n == 10:
                n = 0
                countriestab.append(countriesString[0:-1])
                countriesString = ""
        

        API_KEY =  os.environ.get('API_KEY')
        
        BASE_URL = 'https://holidayapi.com/v1/holidays'

        today = datetime.now()
        for countriesString in countriestab:
            print(countriesString)
            params = {
                "key": API_KEY, 
                "country" : countriesString,
                "year": today.year-1,
                "language": "PL",
            }

            response = requests.get(BASE_URL, params=params)
            if response.status_code == 200:
                holidays = response.json().get("holidays", [])
                if holidays:
                    for holiday in holidays:
                        
                        holiday_name = holiday.get("name")
                        holiday_date = holiday.get("date")
                        holiday_public = holiday.get("public")
                        holiday_country = Country.objects.get(code=holiday.get("country"))

                        holiday_obj, created = Holiday.objects.get_or_create(
                            name = holiday_name,
                            date = holiday_date, 
                            public = holiday_public,
                            country= holiday_country
                        )

                    print(f"{len(holidays)} holidays added/updated in the database.")
            else:
                print(f"Error: {response.status_code} - {response.text}")
