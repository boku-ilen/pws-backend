# pws-backend

Django Back-End for the [ParkWorkingSpaces](https://parkworking.at/) App.

## Setup

1. Install Python
2. Install the requirements: `pip install -r requirements.txt`
3. Install PostgreSQL
4. Setup a database and a user
5. Configure the database values in `pws/settings.py` accordingly
6. Setup the database tables: `python manage.py migrate`
7. Fill the database with initial static data: `python manage.py loaddata tables.json`
8. Run the server: `python manage.py runserver`