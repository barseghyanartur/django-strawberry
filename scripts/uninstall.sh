#!/usr/bin/env bash
pip uninstall django-strawberry -y
rm build -rf
rm dist -rf
rm -rf src/django_strawberry.egg-info
rm -rf src/django-strawberry.egg-info
rm builddocs.zip
rm builddocs/ -rf
