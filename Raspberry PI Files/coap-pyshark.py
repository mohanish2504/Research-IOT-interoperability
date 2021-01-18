import pyshark
import datetimes
#coap-pyshark
def packet_captured_coap(packet):
	a = datetime.datetime.now()
	coap_layers = packet.get_multiple_layers('coap')
	if coap_layers:
		msg = coap_layers[0].get_field_by_showname('Payload')
		#msg = msg.get_default_value() 
		if msg:
			print('Message : ',msg.binary_value.decode('ascii'))
			#b = datetime.datetime.now()
			#print(b-a)

coap_capture = pyshark.LiveCapture(interface='lo')
coap_capture.apply_on_packets(packet_captured_coap)

