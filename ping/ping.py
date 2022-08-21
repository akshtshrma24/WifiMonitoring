import subprocess
import time

from logger import * 

#pings the ip given, sends 2 packets, gets the output as byte type,
#converts to String, and returns it
def pingIP(ip, packets):
    return str(subprocess.Popen(f'ping -c{packets} {ip}' , stdout=subprocess.PIPE, shell=True).communicate()[0])

#keeps pinging every 30 seconds until connection restablished 
#Pings Google DNS To ensure connection stability
#exits once it is restablished, sends logs periodically 
def halt():
    time.sleep(30)
    packetLoss = parsePing(pingIP('8.8.8.8', 10))[2]
    if(packetLoss > 0):
        error(f"Still PacketLoss: {packetLoss}")
        halt()
    success("Connection reestablished")
    
#parses the output given for packets trasnmitted, 
#receieved and packetLoss in percent
def parsePing(output):
    output = output.split(" ")
    for a in output:
        match a:
            case 'packets':
                transmitted = int(output[output.index(a) - 1].split('\\n')[1])
            case 'received,':
                received = int(output[output.index(a) - 1])
            case 'packet':
                packetLoss = float(output[output.index(a) - 1][0:-1])
    if(packetLoss > 0): 
        halt()
    return [transmitted, received, packetLoss]
        