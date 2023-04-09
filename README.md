# mygarden

Django app that tracks my vegetable gardens.  

Use case is to help remind me when I should harvest and what I currently have planted.

## Features

* Add the gardens their plants that you're tracking
* View the status of the plants that you will need to harvest based on dates

## Running Locally

### Do once the first time
```sh
$ pip3 install -r requirements.txt
$ DJANGO_SUPERUSER_PASSWORD=testpass1234 python3 manage.py createsuperuser --noinput --username admin --email email@email.com
```

### To startup the server
```sh
$ DEBUG=true python3 manage.py runserver
```
