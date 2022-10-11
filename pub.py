from http import client
from pydoc import cli
import time
import paho.mqtt.client as mqtt_client
import random

broker = "broker.emqx.io"

client = mqtt_client.Client(f'lab_{random.randint(10000, 99999)}')

client.connect(broker)
client.publish('lab/room1/sensor', random.randint(100, 999))
