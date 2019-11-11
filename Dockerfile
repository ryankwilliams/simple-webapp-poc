FROM python:3.6-alpine

ENV APP_DIR=/opt/app
ENV SRC_DIR=${APP_DIR}/src

RUN apk --no-cache add bash nginx

RUN /bin/bash -c "mkdir -p ${APP_DIR}/{nginx,logs} /var/cache/nginx"

COPY . ${SRC_DIR}/
COPY nginx/nginx.conf /etc/nginx/nginx.conf
COPY nginx/app.conf /etc/nginx/conf.d/app.conf

RUN chmod -R g+rwx /var/log/nginx /var/cache/nginx ${APP_DIR}/nginx && \
    chgrp -R root /var/log/nginx /var/cache/nginx ${APP_DIR}/nginx && \
    chmod -R g+rwx ${APP_DIR}/ && \
    chown -R nginx:root ${APP_DIR} && \
    chmod -R g=u ${APP_DIR} /etc/passwd

RUN pip --no-cache-dir install -r ${SRC_DIR}/requirements.txt

RUN addgroup nginx root

WORKDIR ${SRC_DIR}

EXPOSE 8081

CMD gunicorn -w 1 -b 0.0.0.0:8081 --capture-output \
    --log-file ${APP_DIR}/logs/output.log \
    --access-logfile ${APP_DIR}/logs/access.log \
    wsgi:app && nginx -g 'daemon off;'
