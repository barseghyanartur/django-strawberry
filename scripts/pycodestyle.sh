#!/usr/bin/env bash
reset
pycodestyle src/strawberry/ --exclude migrations,south_migrations
