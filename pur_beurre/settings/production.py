from pur_beurre.settings.base import *

import sentry_sdk
import cronitor

from sentry_sdk.integrations.django import DjangoIntegration
from django.core.management import call_command

# Sentry
sentry_sdk.init(
    dsn=os.getenv('SENTRY_DSN'),
    integrations=[DjangoIntegration()],

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0,

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
)

# Cronitor

cronitor.api_key = os.getenv('CRONITOR_KEY')


# monitor any function
@cronitor.job('QWpptg')
def update_database(args):
    call_command('update_database')


# Or embed telemetry events in your application
monitor = cronitor.Monitor('QWpptg')
# send a run event (a job/process has started)
monitor.ping(state='run')
# send a complete event (a job/process has completed successfully)
monitor.ping(state='complete')
# send a failure event
monitor.ping(state='fail')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["178.62.109.10"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'pur_beurre',
        'USER': 'clelio',
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}