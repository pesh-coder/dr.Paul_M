#!/usr/bin/env bash
set -e

# Run DB migrations
python manage.py migrate --noinput

# One-time superuser creation / update (safe to leave in)
if [[ -n "$DJANGO_SUPERUSER_USERNAME" && -n "$DJANGO_SUPERUSER_EMAIL" && -n "$DJANGO_SUPERUSER_PASSWORD" ]]; then
  python manage.py shell <<'PY'
import os
from django.contrib.auth import get_user_model
U = get_user_model()

username = os.environ["DJANGO_SUPERUSER_USERNAME"]
email = os.environ["DJANGO_SUPERUSER_EMAIL"]
password = os.environ["DJANGO_SUPERUSER_PASSWORD"]

u, created = U.objects.get_or_create(
    username=username,
    defaults={"email": email, "is_staff": True, "is_superuser": True},
)

changed = False
if not u.is_superuser or not u.is_staff:
    u.is_superuser = True
    u.is_staff = True
    changed = True
if u.email != email:
    u.email = email
    changed = True
u.set_password(password)
changed = True
if changed:
    u.save()

print("Superuser ready:", username, "| created:", created)
PY
fi

# Collect static files
python manage.py collectstatic --noinput

# Start app
gunicorn dr_paulM.wsgi:application --bind 0.0.0.0:$PORT --workers 3 --timeout 120
