import pyshark
import datetime
#coap-pyshark

class CoAP:
    messages = dict()

    def __init__(self,childProcess):
        self.childProcess = childProcess

    def packet_captured_coap(self,packet):
        t = datetime.datetime.now().time()
        datagram = {}
        coap_layers = packet.get_multiple_layers('coap')
        
        if coap_layers:
            
            method = coap_layers[0].get_field_by_showname('Code')
            if method == '1' or method == '4':return

            #print(coap_layers[0])

            msg_id = coap_layers[0].get_field_by_showname('Message ID')
            if msg_id in self.messages.keys(): return

            topic = coap_layers[0].get_field_value('opt_uri_path_recon')
            if 'fromMQTT' in topic:return
            
            #print(method,msg_id,sep=' ')
            msg = coap_layers[0].get_field_by_showname('Payload')
            msg = msg.binary_value.decode('ascii')
            
            
            datagram['Type'] = "Post"
            datagram['Message'] = msg
            datagram['Topic'] = topic[1:]
            
            if self.messages:
                self.messages= {}
            
            self.messages[msg_id] = datagram

            self.childProcess.send(datagram)

            

            
def startCoAP(childProcess):    
    obj = CoAP(childProcess)
    coap_capture = pyshark.LiveCapture(interface='wlan0')
    coap_capture.apply_on_packets(obj.packet_captured_coap)     

