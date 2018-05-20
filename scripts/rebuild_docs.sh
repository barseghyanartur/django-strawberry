#!/usr/bin/env bash
rm docs/django_strawberry*.rst
rm -rf builddocs/
sphinx-apidoc src/strawberry --full -o docs -H 'django-strawberry' -A 'Artur Barseghyan <artur.barseghyan@gmail.com>' -V '0.1' -f -d 20
cp docs/conf.py.distrib docs/conf.py

./scripts/build_docs.sh
