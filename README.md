

## Description
Simple website with two pages: list of users and list of groups

## Technologies
* Python (3.7.0)
* sqlite3
* Django (2.1.7)


## Install
For the next steps of service installation, you will need setup of Ubuntu OS


### Install and configure sqlite3 server on your local machine:
```
sudo apt update
sudo apt install sqlite3
sudo apt install php-sqlite3
sudo service apache2 restart
```


### Install project
* Create a new virtual environment with `Python 3.7.0` (using `pyenv` or another tool).
* Clone this repository to your local machine


### Django
* Go to the folder with `manage.py` file and run migrate files
```
python manage.py makemigrations
python manage.py migrate
```

* Go to the folder with `manage.py` file, run django server 
```
python manage.py runserver
```


