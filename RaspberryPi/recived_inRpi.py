import paho.mqtt.client as mqtt
import time
import json
import requests


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

    # If we lose the connection and reconnect then subscriptions will be renewed.
    client.subscribe([("esp32_2021", 1), ("ep_mqtt/topic1", 1)])


def on_message(client, userdata, message):
    m_decode=str(message.payload.decode("utf8"))
    message=json.loads(m_decode)
    print(message)
    r=requests.post('http://webapi19sa-1.course.tamk.cloud/v1/weather',json=message)
    print(r.text) #will show data is created in api or not
    print(r)      #if status is 201 data succesfully posted 
    

broker_address = "10.5.1.201"  # raspi own ip
port = 1883 # Broker port

client = mqtt.Client()  # create new instance
client.on_connect = on_connect  # attach function to callback
client.on_message = on_message  # attach function to callback

client.connect(broker_address, port)  # connect to broker

client.loop_forever()