FROM python:3.9-slim

WORKDIR /app

# מעתיק את הדרישות ומתקין אותן
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# מעתיק את app.py וכל השאר
COPY . .

EXPOSE 5000

CMD ["python", "app.py"]