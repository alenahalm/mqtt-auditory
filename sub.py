import time
import paho.mqtt.client as mqtt_client
import random


def on_message(client, userdata, message):
    data = str(message.payload.decode("utf-8"))
    # topic = str(message.topic.decode("utf-8"))
    print(f"Received message: {data}")


broker = "broker.emqx.io"

client = mqtt_client.Client(f'lab_{random.randint(10000,99999)}')
client.on_message = on_message

try:
    client.connect(broker)
except Exception:
    print('Failed to connect. Check network')
    exit()

client.loop_start()

# while not client.is_connected():

client.subscribe('lab/room1/sensor')
print('Subscribing')
time.sleep(600)
client.disconnect()
client.loop_stop()

print('Stop communication')
