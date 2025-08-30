# Use a small base image
FROM python:3.10-slim

WORKDIR /code

# copy & install dependencies
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

# copy app code
COPY . /code

EXPOSE 8000

# use gunicorn in production; it will serve app:app
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app:app"]

