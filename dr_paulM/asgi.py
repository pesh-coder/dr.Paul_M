"""
ASGI config for dr_paulM project.
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dr_paulM.settings')

application = get_asgi_application()
