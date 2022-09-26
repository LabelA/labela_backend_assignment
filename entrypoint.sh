#!/bin/sh

echo "Waiting for postgres..."
set -e

host="$1"
shift

pip install --no-cache-dir -r requirements.txt

until PGPASSWORD=$POSTGRES_PASSWORD psql -h "$host" -U "autocompany" -c '\q'; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

>&2 echo "Postgres is up - executing command"

echo "PostgreSQL started"

# python manage.py flush --no-input
# PGPASSWORD=autocompany psql --host db --port 5432 --username=autocompany --dbname=autocompany < tracdb/trac.sql

python manage.py migrate

python manage.py collectstatic --no-input --clear

python manage.py loaddata fixtures/*

#if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ] ; then
#    (python manage.py createsuperuser --noinput)
#fi
python manage.py initadmin
# python manage.py update_docs
exec "$@"