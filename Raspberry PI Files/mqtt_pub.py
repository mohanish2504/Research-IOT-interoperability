import paho.mqtt.client as paho

broker="192.168.31.68"
port=1883

def on_publish(client,userdata,result):             #create function for callback
    #print("data published \n")
    pass

def mqttPub(msg,topic):
	#print(topic)
	#topic = topic.strip('fromWEB')
	#print(topic)
	client1= paho.Client("control1")                           #create client object
	client1.on_publish = on_publish                          #assign function to callback
	client1.connect(broker,port)                                 #establish connection
	ret= client1.publish(topic,msg)   
	