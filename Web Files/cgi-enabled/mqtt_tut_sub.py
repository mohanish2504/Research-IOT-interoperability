import paho.mqtt.client as mqtt
import time 
import multiprocessing as mp

localhost = "0.0.0.0"
port = 1883


print("creating new instance")
client = mqtt.Client("P1")


def on_message(client,userdata,message):
	print("message received " ,str(message.payload.decode("utf-8")))
	print("message topic=",message.topic)
	print("message qos=",message.qos)
	print("message retain flag=",message.retain)

client.on_message=on_message

print("connecting to broker")

print("Subscribing to topic","Light")
print("connecting to MQTT")
client.connect(localhost,port)
#print("Name : PONTE"," port : ",port)
client.subscribe("Light")
client.loop_forever()