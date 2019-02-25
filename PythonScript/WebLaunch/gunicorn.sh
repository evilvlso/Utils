#!/bin/bash
Bind=0.0.0.0:3000
APP=app:app
ProPath=`pwd`
Exe_Path=`which gunicorn`
##############
exec $Exe_Path \
--workers 10 \
--threads 5 \
--bind $Bind \
--worker-connections 50 \
--worker-class gevent \
--pid "/var/run/gunicorn.pid" \
--access-logfile $ProPath/log/gunicorn_access.log  \
--max-requests 100 \
--error-logfile $ProPath/log/gunicorn_error.log \
--log-level warning \
--reload \
$APP