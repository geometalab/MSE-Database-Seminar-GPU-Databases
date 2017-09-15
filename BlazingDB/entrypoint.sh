#!/bin/bash

service cron start
/usr/bin/supervisord

exec "$@"