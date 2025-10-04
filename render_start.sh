#!/usr/bin/env bash
set -e

# Run DB migrations every time the service boots
python manage.py migrate --noinput

# Start the app (use 1 worker because you're on SQLite)
gunicorn dr_paulM.wsgi:application \
  --bind 0.0.0.0:${PORT} \
  --workers 1 \
  --timeout 120
