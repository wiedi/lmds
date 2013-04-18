import os
import django.core.handlers.wsgi

# Django
os.environ['DJANGO_SETTINGS_MODULE'] = 'lmds.settings'
application = django.core.handlers.wsgi.WSGIHandler()
