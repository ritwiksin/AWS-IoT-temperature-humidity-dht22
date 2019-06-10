# AWS-IoT-temperature-humidity-dht22

Reads Temperature and Humidity using the DHT22 sensor on a Raspberry PI and sends it to AWS IoT.


The GrovePi is an open-source platform for connecting Grove Sensors to the Rasberry Pi.
This script reads the room temperature and humidity using the DHT-22 sensors and sends it to AWS IoT.

This data can then be sent to Elasticsearch and we can create a Timelion graph for Temperature and Humidity on Kibana.
We can also use Quicksight for creating graphs for this.

Once the setup of GrovePi is complete, connect the DHT-22 sensor to any port.  
For example, I have used Port 7.

Now, create a AWS IoT thing using the official guide:

https://docs.aws.amazon.com/iot/latest/developerguide/sdk-tutorials.html#iot-sdk-create-thing

Make sure to download the Certificates.

Now, go edit the script to add your details:

```javascript
mqtt_topic = "helloTopic"
mqtt_host = "*******.iot.us-west-2.amazonaws.com"
ca_root_cert_file = "root-CA.crt"
thing_cert_file = "GroveThing.cert.pem"
thing_private_key = "GroveThing.private.key"
```

Now, run the script. You should be receiving the Temperature and Humidity data in your AWS IoT.
