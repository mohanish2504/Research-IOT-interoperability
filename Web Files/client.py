from coapthon.client.helperclient import HelperClient
from coapthon import defines

class CoAP:
	messages = {} 
	def __init__(self,msg,topic):
		host = "192.168.31.68"
		port = 5683
		ct = {'content_type': defines.Content_types["application/link-format"]}
		client = HelperClient(server=(host, port))
		path = topic+"fromWEB"
		payload = msg
		response = client.post(path,payload)
		client.stop()
		#print('i m returning from here')

def coapPost(msg,topic):
	coap = CoAP(msg,topic)

#coapPost('on','HelloCoAP')
