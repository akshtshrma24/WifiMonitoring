import subprocess

from logger import * 

#pings the ip given, sends 2 packets, gets the output as byte type,
#converts to String, and returns it
def pingIP(ip, packets):
    return str(subprocess.Popen(f'ping -c{packets} {ip}' , stdout=subprocess.PIPE, shell=True).communicate()[0])


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
        error("Packets Lost", packetLoss, f"Sent: {transmitted} Received: {receieved}")
    return [transmitted, received, packetLoss]
        