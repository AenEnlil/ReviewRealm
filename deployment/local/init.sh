

sleep 15s &&
python manage.py migrate && \
python seeding.py && \
python manage.py runserver 0.0.0.0:8000