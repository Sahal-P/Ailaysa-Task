[![Python 3.11](https://img.shields.io/badge/python-3.11-yellow.svg)](https://www.python.org/downloads/release/python-360/)
![Django 5.0](https://img.shields.io/badge/Django-5.0-green.svg)
![Django 5.0](https://img.shields.io/badge/DRF-5.0-red.svg)
![Celery 5.0](https://img.shields.io/badge/Celery-5.3.6-green.svg)
![Redis](https://img.shields.io/badge/Redis-red.svg)
![Postgresql 5.0](https://img.shields.io/badge/Postgresql-blue.svg)


# Ailaysa Task
Backend - python using django rest framework

Database - postgreSQL 

## Installation

**1.clone Repository & Install Packages**
```sh
git clone https://github.com/Sahal-P/Ailaysa-Task

cd Ailaysa-Task/apps/api/


```
**2.create .env file from .env.example**
```sh
SECRET_KEY=
DEBUG=

DATABASE_NAME=
DATABASE_USER=
DATABASE_PASS=
DATABASE_HOST=
DATABASE_PORT=

REDIS_URL=
CACHE_REDIS_URL=

STATIC_URL=
MEDIA_ROOT=
MEDIA_URL=

USE_S3=
S3_KEY_ID=
S3_SECRET_ACCESS_KEY=
S3_BUCKET_NAME=
S3_HOST=
S3_REGION_NAME=

DEFAULT_PASSWORD=
```
**3. Start Server**
```sh
python manage.py runserver

celery -A core worker -l info -P gevent
```
**3. Or using docker-compose**
```sh
docker-compose up --build

```

## Where to find Me
[Linkedin](https://www.linkedin.com/in/sahal-p-ba81a2260/)

## API Response Example

![ Api Put Example](https://utfs.io/f/16249a72-824c-4e06-bfd1-05d384f886d1-6i1yv7.jpg)
![ Api Get Example](https://utfs.io/f/50b10584-965a-406a-ab5b-5ded766b48d5-axco3g.jpg)
![ Api Post Example](https://utfs.io/f/d5059657-2605-421e-840c-4cb384555351-16bfvu.jpg)


