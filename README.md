# ChatterBot Django Live Example

This is an example Django app that shows how to create a simple chat bot web
app using [Django](https://ww.djangoproject.com) and [ChatterBot](https://github.com/gunthercox/ChatterBot).

## Quick Start

Clone this repository:

``` Bash
git clone \<repo\>
cd \<repo\>
```

Ramp up virtual environment (very much recommended)
``` Bash
python3 -m virtualenv venv
source venv/bin/activate
```

Intall requirements
``` Bash
pip3 install -r requirements.txt
```

Generate a new Django SECRET_KEY, e.g. via https://miniwebtool.com/django-secret-key-generator
Then:
``` Bash
export DJANGO_SECRET_KEY='<secret_key>'
echo SECRET_KEY='<secret_key>' > .env
```

Django first-time initialization

``` Bash
python manage.py migrate --run-syncdb
python manage.py migrate train
```

Start the Django app by running 

``` Bash
python manage.py runserver 0.0.0.0:8000
```

Further documentation on getting set up with Django and ChatterBot can be found in the [ChatterBot documentation](http://chatterbiot.readthedocs.io/en/latest/django.html)

## Make migrations

``` Bash
python manage.py migrate
```
## Train your bot

``` Bash
python manage.py train
```

## Training Corpus Path
The chatterbot [corpus path](https://github.com/gunthercox/chatterbot-corpus/tree/master/chatterbot_corpus/data/english) can be found here.

## Bot Django Settings
You could found Bot settings [here](./example_app/settings.py)

``` Python
CHATTERBOT = {
    'name': 'Heroku ChatterBot Example',
    'logic_adapters' : [
        "chatterbot.logic.BestMatch"
    ],
    'trainer': 'chatterbot.trainers.ChatterBotCorpusTrainer',
    'training_data': [
        'chatterbot.corpus'
    ]
}
```

### Allowed Hosts
Include your address at the ALLOWED_HOSTS directives in settings.py - Just the domain, make sure that you will take the protocol and slashes from the string

for example
``` Python
ALLOWED_HOSTS = ['127.0.0.1', 'chatterbot-demo.herokuapp.com']
```
    
## Deploying on Heroku

### Creating a new Heroku app

heroku create
Creating intense-falls-9163... done, stack is cedar
http://intense-falls-9163.herokuapp.com/ | git@heroku.com:intense-falls-9163.git
Git remote heroku added

### Heroku CLI

Before deploying Heroku you should install Heroku CLI on your machine, documentation found here https://devcenter.heroku.com/articles/heroku-cli

Login:

``` Bash
heroku login
```
Enter your Heroku credentials.
...

### Deploying

``` Bash
git add .

git commit -m "<comment>"

git push heroku master

heroku run python manage.py migrate
heroku run python manage.py train
```

A more detailed information can be found here https://devcenter.heroku.com/articles/deploying-python

## LICENSE
ChatterBot Django Live Example is licensed under [BSD 3-clause](./license.md)

