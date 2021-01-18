import pyshark
import datetime
import threading
from multiprocessing import Process,Queue,Pipe
from mqtt_pyshark import startMQTT
from coap_pyshark import startCoAP
from mqtt_pub import mqttPub
from coap_client import coapPost

mainProcessMQTT,childProcessMQTT = Pipe()
mainProcessCoAP,childProcessCoAP = Pipe()

#import requests

#url = 'http://localhost/cgi-enabled/index.py'

#ef coapProcess(msg,topic):coapPost(msg,topic)

def P1():
	p1 = Process(target=startMQTT,args=(childProcessMQTT,))
	p1.start()
	while True:
		datagram = mainProcessMQTT.recv()
		if datagram:
			#print('From MqttSide : ',i)
			print(datagram)
			temp = datagram
			datagram = None
			coapPost(temp['Message'],temp['Topic'])
			query = temp
			#res = requests.post(url, data=query)
			#print(res.text)
			#print(datagram)


def P2():
	p2 = Process(target=startCoAP,args=(childProcessCoAP,))
	p2.start()
	while True:
		datagram = mainProcessCoAP.recv()
		#print(datagram)
		if datagram:
			#print('From CoapSide')
			temp = datagram.copy()
			datagram['Topic'] = datagram['Topic'].strip('fromWEB')
			print(datagram)
			datagram = None
			#print(temp)
			mqttPub(temp['Message'],temp['Topic'])
			#query = temp
			#res = requests.post(url, data=query)
			#print(res.text)



Pr1 = Process(target = P1)
Pr1.start()
Pr2 = Process(target=P2)	
Pr2.start()

