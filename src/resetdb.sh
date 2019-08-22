poetry shell
python manage.py migrate app zero
rm -fr app/migrations
mkdir app/migrations
touch app/migrations/__init__.py
python manage.py makemigrations
python manage.py migrate
python manage.py make_seed
python manage.py loaddata seed.json
