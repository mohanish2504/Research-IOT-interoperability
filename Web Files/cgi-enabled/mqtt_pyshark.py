import pyshark
import datetime
from multiprocessing import Process,Pipe

#mqtt-pyshark
class MQTT:
	def __init__(self,childProcess):
		self.childProcess = childProcess

	def packet_captured_mqtt(self,packet):
		a = datetime.datetime.now()
		datagram = {}
		mqtt_layers = packet.get_multiple_layers('mqtt')
		if mqtt_layers:
			msgtype = mqtt_layers[0].get_field('msgtype')
			#print(msgtype)
			topic = mqtt_layers[0].get_field_by_showname('Topic')
			#print(topic,'MQTT')
			if msgtype == '3' and 'fromWEB' not in topic and topic != None:
				msg = mqtt_layers[0].get_field_by_showname('Message')
				if msg:
					datagram['Type'] = "Publish"
					datagram['Message'] = msg
					datagram['Topic'] = topic		
					self.childProcess.send(datagram)
			
			'''if msgtype == '8':
				datagram['Type']="Subscribe"
				datagram['Topic']=topic
				self.childProcess.send(datagram)'''

def startMQTT(childProcess):
	mqtt_capture = pyshark.LiveCapture(interface='wlan0')
	obj = MQTT(childProcess)
	mqtt_capture.apply_on_packets(obj.packet_captured_mqtt)
