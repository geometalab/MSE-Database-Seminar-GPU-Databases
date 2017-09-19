#!/bin/sh
mkdir /data
mkdir /data/db
chown postgres:postgres /data
chown postgres:postgres /data/db/
chown postgres:postgres /opt/pg-strom/postgresql.conf
chmod 755 /data
chmod 755 /data/db
su - postgres -c "/usr/lib/postgresql/9.5/bin/initdb -D /data/db"
cp /opt/pg-strom/postgresql.conf /data/db/postgresql.conf
echo /usr/local/cuda/lib64 > /etc/ld.so.conf.d/cuda-x86_64.conf
ldconfig
su - postgres -c "/usr/lib/postgresql/9.5/bin/pg_ctl -D /data/db start"
