#!/bin/sh

# Load initial data (fixtures)
echo "Load initial data"

# Collecting static
echo "Collecting static ..."
python manage.py collectstatic

# Start server
echo "Starting server ..."
python manage.py runserver 0.0.0.0:8000
