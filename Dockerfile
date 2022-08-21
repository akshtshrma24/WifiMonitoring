FROM python:3.10.1

WORKDIR /ping_monitoring

RUN apt-get update; echo "y" | apt-get install iputils-ping

RUN pip3 install --upgrade pip

RUN pip3 install requests

COPY /ping/ .

COPY /influx/ .

COPY /scraper/ .

COPY logger.py . 

#Pinging Google's Public DNS Server
# <IP> <packets you sant to send> <scrape interval>
CMD ["python3","scraper.py", "8.8.8.8", "10", "50"]
