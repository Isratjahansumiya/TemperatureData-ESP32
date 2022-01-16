from umqtt.simple import MQTTClient
from machine import Pin, ADC, I2C
import machine
import ssd1306
import time
import ubinascii
import machine
import micropython
import network
import json
import esp
esp.osdebug(None)
import gc
gc.collect()

vn= Pin(36, Pin.IN)

mqtt_server = '10.5.1.201' #raspi ip
port = 1883                # Broker port
interval=20

client_id = ubinascii.hexlify(machine.unique_id())
topic_sub = b'esp32_2021'
topic_pub = b'esp32_2021'


last_message = 0
message_interval = 5
counter = 0

#connecting to wifi
station = network.WLAN(network.STA_IF)
station.active(True)
#station.connect('Koti_2089','HRMQ8UNMR3H3F')
station.connect('SOURCE','Pelle!23')
while station.isconnected() == False:
  pass

print('Esp wifi connection successful')
print(station.ifconfig())

#getting adc value
adc = ADC(vn)
adc.atten(ADC.ATTN_11DB)    # set 11dB input attenuation (voltage range roughly 0.0v - 3.6v)
adc.width(ADC.WIDTH_10BIT)   # set 10 bit return values (returned range 0-1023)
adc_value=adc.read()

#printing temperature in oled
i2c = I2C(-1, scl=Pin(4), sda=Pin(5))
oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)
oled.fill(0)
#voltage divider was used to convert 5v into 3.3v: 120Ohm (R1) and 220Ohm (R2)
vol_in= ((adc_value)*3.3)/1023
oled.text("V in (3.3v): "+str(vol_in), 0, 0)
vol_out=((adc_value)*3.3*34/22)/1023
temperature=float("{:.1f}".format((vol_in -.5)*10))
oled.text("V out (5v): "+str(vol_out), 0, 10)
print("Temparature: ",temperature,"degrees C")
oled.text("Temp :"+str(temperature), 0, 20)
oled.show()


def sub_cb(topic, msg):
  print((topic, msg))
  if topic == b'esp32_2021':
   print('sending...')

def connect_and_subscribe():
  global client_id, mqtt_server, topic_sub, port
  client = MQTTClient(client_id, mqtt_server,port)
  client = MQTTClient(client_id, mqtt_server)
  client.set_callback(sub_cb)
  client.connect()
  client.subscribe(topic_sub)
  print('Connected to %s MQTT broker, subscribed to %s topic' % (mqtt_server, topic_sub))
  return client

def restart_and_reconnect():
  print('Failed to connect to MQTT broker. Reconnecting...')
  time.sleep(10)
  machine.reset()

try:
  client = connect_and_subscribe()
except OSError as e:
  restart_and_reconnect()

while True:
  try:
    client.check_msg()
    if (time.time() - last_message) > message_interval:
     msg= json.dumps({"device id": "esp32_2021","Temperature": temperature});
     #print(type(msg)
     client.publish(topic_pub, msg)
     last_message = time.time()
     counter += 1
  except OSError as e:
    restart_and_reconnect()
    
    

