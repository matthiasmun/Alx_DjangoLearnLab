"""
ASGI config for LibraryProject project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
<<<<<<< HEAD
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
=======
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
>>>>>>> eafbf58 (Add initial Django project files)
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')

application = get_asgi_application()
