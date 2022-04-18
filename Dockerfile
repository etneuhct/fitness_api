FROM python:3.9.12-alpine3.15

WORKDIR /usr/src/app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN \
 apk add --no-cache postgresql-libs && \
 apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev libffi-dev
RUN python3 -m pip install -r requirements.txt --no-cache-dir && apk --purge del .build-deps
COPY . .
RUN python manage.py collectstatic

RUN apk --no-cache add nginx
RUN apk add sudo
COPY ./proxy_default.conf /etc/nginx/http.d/default.conf
RUN dos2unix /etc/nginx/http.d/default.conf
RUN chown :0 /var/lib/nginx/ -R
RUN chown :0 /var/log/nginx/ -R
RUN chown :0 /etc/nginx/ -R
RUN chmod 777 /usr/src/app/ -R
EXPOSE 80
EXPOSE 443
CMD sh /usr/src/app/runme.sh
