# django-mailer
The basic mailer application backed by Django

## instructions

### clone this repo
git clone git@github.com:elcanion/django-mailer.git
cd django-mailer/backend/backend

### install django-environ
pipenv shell
pipenv install django-environ

### create an .env file inside backend/backend dir and put this auth info into it
EMAIL_HOST=<your email host>
EMAIL_HOST_USER=<your preferred email>
EMAIL_HOST_PASSWORD=<password>
RECIPIENT_ADDRESS=<your recipient address>
  
### finally, send your email
python manage.py shell
>>> from django.core.mail import send_mail
>>> from django.conf import settings
>>> send_mail('your subject', 'your message', settings.EMAIL_HOST_USER, [settings.RECIPIENT_ADDRESS])
