from pur_beurre.settings.base import *

import sentry_sdk
import cronitor

from sentry_sdk.integrations.django import DjangoIntegration
from django.core.management import call_command

# Sentry
sentry_sdk.init(
    dsn="https://6929f6ed13b141fda268e2aa1629f9eb@o561438.ingest.sentry.io/5698543",
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

cronitor.api_key = '7632b9d120e143969c99bb15f76968da'


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
        'PASSWORD': 'juve1898',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}