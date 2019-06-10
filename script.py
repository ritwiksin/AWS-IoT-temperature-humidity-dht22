# Import packages
import paho.mqtt.client as mqtt
from grovepi import *
from grove_oled import *
import grovepi
import math
import ssl
import time

# Define variables
mqtt_port = 8883
mqtt_keepalive_interval = 45
blue = 0
dht_sensor_port = 7
mqtt_topic = "helloTopic"
mqtt_host = "a12nnunootm2a1.iot.us-west-2.amazonaws.com"
ca_root_cert_file = "root-CA.crt"
thing_cert_file = "GroveThing.cert.pem"
thing_private_key = "GroveThing.private.key"


# Define on publish event function
def on_publish(client, userdata, mid) :
	print ("Temperature and Humidity")


# Initialize MQTT client
mqttc = mqtt.Client()

# Register publish callback function
mqttc.on_publish = on_publish


# Configure TLS set
mqttc.tls_set(ca_root_cert_file, certfile=thing_cert_file, keyfile=thing_private_key, cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)

# Connect with MQTT Broker
mqttc.connect(mqtt_host, mqtt_port, mqtt_keepalive_interval)
mqttc.loop_start()

while True:
	[temp,humidity] = grovepi.dht(dht_sensor_port,blue)
	if math.isnan(temp) == False and math.isnan(humidity) == False:
		print((temp,humidity))
		strData = " ".join(str(x) for x in (temp,humidity))
		mqtt_msg = strData
		mqttc.publish(mqtt_topic,mqtt_msg,qos=1)
		time.sleep(1)

# Disconnect from MQTT_Broker
# mqttc.disconnect()
