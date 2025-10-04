"""
WSGI config for dr_paulM project.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dr_paulM.settings')

application = get_wsgi_application()
