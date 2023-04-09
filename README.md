# mygarden

Django app that tracks my vegetable gardens.  

Use case is to help remind me when I should harvest and what I currently have planted.

## Features

* Add gardens and the plants in the garden
* Overview the status of your garden on when you should begin to harvest based on the date you planted

## Running Locally

### Do once the first time
```sh
pip3 install -r requiremnts.txt
DJANGO_SUPERUSER_PASSWORD=testpass1234 python3 manage.py createsuperuser --noinput --username admin --email email@email.com
```

### To startup the server
```sh
python3 manage.py runserver
```
