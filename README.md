# hrm
python3 -m virtualenv venv
source venv/bin/activate

clone this repo

cd project

python manage.py makemigrations

python manage.py migrate

python manage.py createsuperuser

python manage.py runserver

visit: localhost:8000
