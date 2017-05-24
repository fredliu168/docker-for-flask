FROM python:3.5
MAINTAINER baiyi liu "fred@qzcool.com"
COPY requirements.txt /usr/www/app/
WORKDIR /usr/www/app
RUN pip install -r requirements.txt
CMD ["python"]