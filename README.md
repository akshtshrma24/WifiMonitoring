# WifiMonitoring

This monitors your wifi, it pings Google DNS Server on an interval of 50 seconds. 
This is configurable from the Dockerfile.

<h2> How to Use </h2>
1. Clone this Repo <br>
2. Run `docker compose up --build` inside
3 Optional. Configure the Dockerfile with the ip u want to ping and the interval

<hr>

<h4> Logger.py </h4>
Custom Logger file to add color to logs.
<h4> ToDo: </h4> 
✅ build pinging scraper thing<br>
✅ connect to influx <br>
✅ Prometheus and Cadvisor
✅ Nginx<br>
✅ grafana the data<br>
❌ Add Alerting<br>
❌ Deploy on At Home Pi<br>
