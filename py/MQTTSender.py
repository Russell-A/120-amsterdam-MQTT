import random
import time
import json
import uuid
import source
import os
from paho.mqtt import client as mqtt_client
from datetime import datetime
import math


broker =  'broker.mqttdashboard.com'
port = 1883
# topic = "/sensinact/providers/+/services/+/resources"
topic = "a1"
topic_big = "a1_big"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 1000)}'
print(client_id)
# username = ''
# password = ''

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    def on_disconnect(client, userdata, rc):
        print("disconnedted!")


    client = mqtt_client.Client(client_id)
#     client.username_pw_set(username, password)
    client.on_disconnect = on_disconnect
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def text_message_to_dict_message(path, indx):
    while True:
        if not os.path.exists(path):
            time.sleep(0.15)
        else:
            print(f"message number {indx} is ready to read \n")
            break
    data = dict()
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    data["t"] = current_time
    data["i"] = indx
    with open(path, "r") as file:
        lines = file.readlines()
        for line in lines:
            info = line.split()
            type = info[0]
            id = info[1]
            degree = info[2]
            # direction = info[3]
            # direction = direction[0]
            speed = info[3]
            # xbr = info[5]
            # xtl = info[6]
            # ybr = info[7]
            # ytl = info[8]
            latcenter = info[4]
            loncenter = info[5]
            # data[id] = f"[{type}, {degree},{direction}, {speed}, {xbr}, {xtl}, {ybr}, {ytl}]"
            data[id] = f"[{type}, {id} ,{degree}, {speed}, {latcenter}, {loncenter}]"
    return data


def publish(client):
    data = dict()
    detected_objects = ["person", "bicycle", "car", "truck", "bus"]
    direction = ["N", "S", "W", "E"]
    j = 0
    message_indx = 0
    count = 0
    while True: #loop over your data
        #time.sleep(0.5)
        # for i in range(1, random.randint(1,5)) :
        #     data[random.choice(detected_objects)] = "[" + str(j) + "," + str(random.uniform(1, 150)) + "," + random.choice(direction) + "," + str(random.uniform(1, 3000)) + "," + str(random.uniform(1, 3000)) + "," + str(random.uniform(1, 3000)) + "," + str(random.uniform(1, 3000)) + "," + str(random.uniform(1, 100)) + "]"
        path_to_message = 'messages-with-pedestrains' + f"/{message_indx}.txt"
        data = text_message_to_dict_message(path_to_message,message_indx)
        # os.system(f"rm {path_to_message}")
        msg = json.dumps(data)
        # l = math.floor(len(msg)/2)
        # msg1 = msg[:l]
        # msg2 = msg[l+1:]
        # result = client.publish(topic, msg1)
        # # result: [0, 1]
        # status = result[0]        
        # if status == 0:
        #     #print(f"Send `{msg}` to topic `{topic}`")
        #     print(f"size of the message is {l}")
        # else:
        #     print(f"Failed to send message to topic {topic}")
        # time.sleep(0.1)
        # result = client.publish(topic, msg2)
        # # result: [0, 1]
        # status = result[0]        
        # if status == 0:
        #     #print(f"Send `{msg}` to topic `{topic}`")
        #     print(f"size of the message is {l}")
        # else:
        #     print(f"Failed to send message to topic {topic}")

        result = client.publish(topic, msg)
        status = result[0]        
        if status == 0:
             #print(f"Send `{msg}` to topic `{topic}`")
            print(f"size of the message is {math.floor(len(msg))}")
        else:
           print(f"Failed to send message to topic {topic}")
        time.sleep(0.1)

        
        
        message_indx += 1


def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)


if __name__ == '__main__':
    run()
