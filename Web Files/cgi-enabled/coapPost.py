from coapthon.client.helperclient import HelperClient
from coapthon import defines

class CoAP:
	messages = {} 
	def __init__(self,msg,topic):
		host = "192.168.31.143"
		port = 5683
		ct = {'content_type': defines.Content_types["application/link-format"]}
		client = HelperClient(server=(host, port))
		path = topic+""
		payload = msg
		response = client.post(path,payload)
		client.stop()
		return

def coapPost(msg,topic):
	coap = CoAP(msg,topic)

coapPost('off','Light')
