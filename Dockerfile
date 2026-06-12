# ---------------------------------- WARNING ----------------------------------
# This file is primarily for production use with k8s
# See Dockerfile in subdirectories for dev use with docker-compose
# ---------------------------------- WARNING ----------------------------------

# ---
# build scss in separate image
# ---
FROM node:26-alpine AS css-compile

WORKDIR /app

COPY ./css-compile/package.json ./css-compile/package-lock.json ./
RUN npm ci

COPY ./djnd ./djnd
COPY ./css-compile/src ./src
COPY ./css-compile/postcss.config.js ./css-compile/tailwind.config.js ./

RUN npm run build

# ---
# wagtail image
# ---
# Use an official Python runtime based on Debian 13 "trixie" as a parent image.
FROM python:3.14-slim-trixie

# Add user that will be used in the container.
RUN useradd wagtail

# Port used by this container to serve HTTP.
EXPOSE 8000

# Set environment variables.
# 1. Force Python stdout and stderr streams to be unbuffered.
# 2. Set PORT variable that is used by Gunicorn. This should match "EXPOSE"
#    command.
ENV PYTHONUNBUFFERED=1 \
    PORT=8000

# Install system packages required by Wagtail and Django.
RUN apt-get update --yes --quiet && apt-get install --yes --quiet --no-install-recommends \
    gettext \
    build-essential \
    libpq-dev \
    libmariadb-dev \
    libjpeg62-turbo-dev \
    zlib1g-dev \
    libwebp-dev \
    libicu-dev \
    python3-icu \
    pkg-config \
    libmagickwand-dev \
 && rm -rf /var/lib/apt/lists/*

# Install the application server.
RUN pip install "gunicorn==26.0.0"

# Install the project requirements.
COPY ./djnd/requirements.txt /
RUN pip install -r /requirements.txt

# Use /app folder as a directory where the source code is stored.
WORKDIR /app

# Set this directory to be owned by the "wagtail" user.
RUN chown wagtail:wagtail /app

# Copy the source code of the project into the container.
COPY --chown=wagtail:wagtail ./djnd .

# Copy the compiled CSS from the previous image.
COPY --chown=wagtail:wagtail --from=css-compile /app/djnd/djnd/static/css ./djnd/static/css

# Use user "wagtail" to run the build commands below and the server itself.
USER wagtail

# Set the IPython directory to a temporary folder to avoid permission issues and
# create the default profile directory with the correct user.
ENV IPYTHONDIR=/tmp/ipython
RUN mkdir -p $IPYTHONDIR/profile_default

# Compile locale files.
RUN python manage.py compilemessages

CMD gunicorn djnd.wsgi:application -b 0.0.0.0:8000 --log-level DEBUG
