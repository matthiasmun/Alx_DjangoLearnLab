"""
WSGI config for LibraryProject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
<<<<<<< HEAD
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
=======
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
>>>>>>> eafbf58 (Add initial Django project files)
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')

application = get_wsgi_application()
