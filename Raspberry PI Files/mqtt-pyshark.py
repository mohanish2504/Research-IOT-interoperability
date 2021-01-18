import pyshark
import datetime

#mqtt-pyshark
def packet_captured_mqtt(packet):
	a = datetime.datetime.now()
	mqtt_layers = packet.get_multiple_layers('mqtt')
	if mqtt_layers:
		msg = mqtt_layers[0].get_field_by_showname('Message')
		if msg:
			print('Message : ',msg)
			b = datetime.datetime.now()
			print(b-a)

mqtt_capture = pyshark.LiveCapture(interface='lo')
mqtt_capture.apply_on_packets(packet_captured_mqtt)
