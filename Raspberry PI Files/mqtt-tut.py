import paho.mqtt.client as mqtt

localhost = "0.0.0.0"
port = 1883

client = mqtt.Client("mak-pc");
client.connect(localhost,port,10)
client.publish("house-light","Ok done")

