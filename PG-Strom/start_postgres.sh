#!/usr/bin/env bash
mkdir /data
chmod 755 /data
su postgres
mkdir /data/db
/usr/lib/postgresql/9.5/bin/initdb -D /data/db
cp /opt/pg-strom/postgresql.conf /data/db/postgresql.conf
/usr/lib/postgresql/9.5/bin/pg_ctl -D /data/db start
