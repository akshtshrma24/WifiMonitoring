import constants

import requests

from logger import * 

#returns the response code
def parseResponseCode(code):
    return int(str(code)[-5:-2])


#If it is an error it will print out an error
def isError(code, response):
    if(code > 204):
        error("Error Sending response to influx, Status: ", response, "\n Full Text: ", response.text)

#Creates a database if not created already, logs an error if it doesnt, does not throw
def createDB():
    info("Creating Database if not created already")
    data = 'q=CREATE DATABASE "pingDB"'
    response = requests.post('http://influxDB:8086/query', headers=constants.HEADERS, data=data)
    isError(parseResponseCode(response), response)

#Posts the data passed in the parameter to influxDB, logs an error if it can not does not throw
def postData(data):
    info("Sending Data to Influx")
    toSend = f'pingDB,mytag=pingData transmitted={str(data[0])}\n'
    toSend += f'pingDB,mytag=pingData receieved={str(data[1])}\n'
    toSend += f'pingDB,mytag=pingData packetLoss={float(data[2])}'
    response = requests.post('http://influxDB:8086/write', params=constants.PARAMS, headers=constants.HEADERS, data=toSend)
    isError(parseResponseCode(response), response)
    