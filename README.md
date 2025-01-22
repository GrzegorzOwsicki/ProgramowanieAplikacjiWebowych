Wymagane

asgiref            3.8.1
certifi            2024.12.14
charset-normalizer 3.4.1
Django             5.1.4
idna               3.10
pip                22.2.2
python-dotenv      1.0.1
requests           2.32.3
setuptools         63.2.0
sqlparse           0.5.3
typing_extensions  4.12.2
tzdata             2024.2
urllib3            2.3.0

przygotowanie bazy danych:
python manage.py makemigrations
python manage.py migrate
python manage.py fetchCountries - pobiera kraje z API
python manage.py fetchHolidays - pobiera święta z API na podstawie krajów, jedno użycie wykonuje 26 zapytań

start servera:
python manage.py runserver
