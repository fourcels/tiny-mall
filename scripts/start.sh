#!/usr/bin/env sh

alembic upgrade head

python db.py init-admin

python start.py