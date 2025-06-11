FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Collect static files
# Handled in docker compose prod file
# command: sh -c "python manage.py collectstatic --noinput && gunicorn aura_backend.wsgi:application --bind 0.0.0.0:8000"
#RUN python manage.py collectstatic --noinput

#CMD ["gunicorn", "aura_backend.wsgi:application", "--bind", "0.0.0.0:8000"]