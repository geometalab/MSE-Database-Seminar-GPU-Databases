FROM nvidia/cuda:8.0-runtime-ubuntu14.04

MAINTAINER Samuel Kurath <skurath@hsr.ch>

EXPOSE 8890

COPY blazing-community-installer.sh /opt/BlazingDB/
COPY entrypoint.sh /opt/BlazingDB/
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf


ENTRYPOINT ["./opt/BlazingDB/entrypoint.sh"]

RUN apt-get update \
&& apt-get install wget vim supervisor -y \
&& chmod +x /opt/BlazingDB/blazing-community-installer.sh \
&& chmod +x /opt/OSMstream/entrypoint.sh \
&& ./opt/BlazingDB/blazing-community-installer.sh \
&& chmod +x /opt/BlazingDB/entrypoint.sh \
