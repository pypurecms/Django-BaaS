FROM python:3.6-alpine
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE=PyPureCMS.settings

# Creating working directory
RUN mkdir /usr/local/src
WORKDIR /usr/local/src

# Copying requirements
add . .

RUN apk --no-cache --virtual .build-deps add \
    ca-certificates gcc postgresql-dev linux-headers musl-dev \
    libffi-dev jpeg-dev zlib-dev \
    && pip install -r requirements.txt \
    && find /usr/local \
        \( -type d -a -name test -o -name tests \) \
        -o \( -type f -a -name '*.pyc' -o -name '*.pyo' \) \
        -exec rm -rf '{}' + \
    && runDeps="$( \
        scanelf --needed --nobanner --recursive /usr/local \
                | awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \
                | sort -u \
                | xargs -r apk info --installed \
                | sort -u \
    )" \
    && apk add --virtual .rundeps $runDeps \
    && apk del .build-deps

EXPOSE 8000
CMD [ "python", "manage.py runserver" ]