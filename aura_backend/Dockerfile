FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Collect static files
RUN python manage.py collectstatic --noinput

CMD ["gunicorn", "aura_backend.wsgi:application", "--bind", "0.0.0.0:8000"]