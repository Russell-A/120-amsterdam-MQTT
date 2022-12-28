import random

from paho.mqtt import client as mqtt_client

import traci,os
from util import *

sumoBinary = os.path.join(os.environ['SUMO_HOME'], 'bin', "sumo-gui")
sumoCmd = [sumoBinary, "-n", "/Users/Res_proj/Documents/Research/120-amsterdam/map/map.net.xml", 
"--step-length", str(0.1),"--start", '--log', './log_file.txt', '--num-clients' , '2']
traci.start(sumoCmd, port = 3400)
traci.setOrder(1)







broker = 'broker.mqttdashboard.com'
port = 1883
topic = "a1"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 100)}'
print(client_id)
# username = ''
# password = ''


def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
#     client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        # print("into on_message")
        # print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

        received_str = msg.payload.decode()
        if (received_str.startswith('{') and received_str.endswith("}")):
            # print(received_str)
            import re
            res = re.findall(r'\[(.*?)\]',received_str)
            print(res)



            traci.simulationStep()
            running_car = set(str(e) for e in traci.vehicle.getIDList())
            car_in_frame = set()
            for item in res:
                typecar, id ,degree, speed, lat, lon = item.split(",")
                id = str(int(id))
                degree = float(degree)
                speed = float(speed)
                x = float(lat)
                y = float(lon)
                position = (x, y)
                car_in_frame.add(id)
                if id in running_car:
                    UpdateVehicle(id,speed, position, degree)
                else:
                    AddVehicle(id,speed, position,typecar)
            for item in running_car - car_in_frame:
                RemoveVehicle(item)



        # print("out  on_message")
        




    client.subscribe(topic)
    client.on_message = on_message


def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()


if __name__ == '__main__':
    run()
