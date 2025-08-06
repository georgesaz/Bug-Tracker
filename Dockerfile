# Use Python 3.10 slim image
FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install gcc and python3-dev needed for some dependencies
RUN apt-get update && apt-get install -y gcc python3-dev && rm -rf /var/lib/apt/lists/*

# Copy requirements and install
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the whole app folder as a package named 'app'
COPY app /app/app

# Copy run.py at /app level
COPY run.py /app/

EXPOSE 80

CMD ["gunicorn", "--bind", "0.0.0.0:80", "app:app"]
