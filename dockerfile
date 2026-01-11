FROM python:3.12-slim

WORKDIR /app

COPY weather_warning.py .
COPY test_weather_warning.py .

RUN pip install pytest

ENTRYPOINT ["python", "weather_warning.py"]
