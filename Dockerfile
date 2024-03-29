FROM python:3.11.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY ./config/requirements.txt /app
COPY . /app

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /app/apps/api

# COPY ./scripts/entrypoint.sh /entrypoint.sh

# RUN chmod +x /entrypoint.sh
# ENTRYPOINT ["/entrypoint.sh"]


