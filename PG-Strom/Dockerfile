FROM nvidia/cuda:8.0-runtime-ubuntu16.04

MAINTAINER Samuel Kurath <skurath@hsr.ch>

EXPOSE 8890 40001

COPY entrypoint.sh /opt/pg-strom/
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf


ENTRYPOINT ["./opt/pg-strom/entrypoint.sh"]

RUN apt-get update \
&& apt-get install wget vim supervisor -y \
&& deb http://apt.postgresql.org/pub/repos/apt/ xenial-pgdg main \
&& apt-get install postgresql-9.6 \
&& cd /opt/pg-strom/ \
&& git clone https://github.com/pg-strom/devel.git pg_strom \
&& cd pg_strom \
&& make \
&& make install \
&& chmod +x /opt/pg-strom/entrypoint.sh \
&& ./opt/BlazingDB/blazing-community-installer.sh \
