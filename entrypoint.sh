#!/bin/sh

gunicorn book.wsgi:application --bind 0.0.0.0:8000