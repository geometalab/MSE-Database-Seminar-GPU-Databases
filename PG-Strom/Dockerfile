FROM nvidia/cuda:8.0-runtime-ubuntu16.04

MAINTAINER Samuel Kurath <skurath@hsr.ch>

EXPOSE 5432

COPY entrypoint.sh /opt/pg-strom/
COPY postgresql.conf /opt/pg-strom/
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf


ENTRYPOINT ["./opt/pg-strom/entrypoint.sh"]

RUN apt-get update \
&& apt-get install software-properties-common -y \
&& add-apt-repository "deb http://apt.postgresql.org/pub/repos/apt/ xenial-pgdg main" \
&& wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add - \
&& apt-get update \
&& apt-get install wget vim supervisor -y \
&& apt-get install postgresql-9.6 -y \
&& apt-get install postgresql-client -y \
&& cd /opt/pg-strom/ \
&& git clone https://github.com/pg-strom/devel.git pg_strom \
&& cd pg_strom \
&& make \
&& make install \
&& chmod +x /opt/pg-strom/entrypoint.sh \
&& mv /opt/pg-strom/postgresql.conf /etc/postgresql/9.6/main/postgresql.conf \
