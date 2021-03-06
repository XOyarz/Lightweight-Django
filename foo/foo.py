import sys
import os

from django.conf import settings 

DEBUG = os.environ.get('DEBUG', 'on') == 'on'

SECRET_KEY = os.environ.get('SECRET_KEY', '!#dnf-6#m0th+(!**iz1t+5@70y0#!@5m^n!5x%-aq-&ovm--v')

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '127.0.0.1:8000',).split(',')

settings.configure(
	DEBUG=DEBUG,
	SECRET_KEY=SECRET_KEY,
	ALLOWED_HOSTS=ALLOWED_HOSTS,
	ROOT_URLCONF=__name__,
	MIDDLEWARE_CLASSES=(
		'django.middleware.common.CommonMiddleware',
		'django.middleware.csrf.CsrfViewMiddleware',
		'django.middleware.clickjacking.XFrameOptionsMiddleware',
	),
)


from django.conf.urls import url
from django.core.wsgi import get_wsgi_application
from django.http import HttpResponse


def index(request):
	return HttpResponse('Hello World')

urlpatterns = (
	url(r'^$', index),
)

application = get_wsgi_application()

if __name__ == "__main__":
	from django.core.management import execute_from_command_line

	execute_from_command_line(sys.argv)