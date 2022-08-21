import sys
import time

from ping import * 
from influxHandler import * 
from logger import * 

#create Database if not already created
createDB()
    
info("Starting the Monitoring, Pinging: ", sys.argv[1], " On interval ", sys.argv[3])

while(True):
    postData(parsePing(pingIP(sys.argv[1],sys.argv[2])))
    time.sleep(int(sys.argv[3]))
