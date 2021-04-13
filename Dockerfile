FROM odoo:13.0

LABEL MAINTAINER Daniel Moreno <contacto@escuelafullstack.com>
USER root

RUN pip3 install pandas
RUN pip3 install numpy
RUN pip3 install beautifulsoup4

