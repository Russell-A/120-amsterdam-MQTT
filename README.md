# 120-amsterdam-mqtt

# BRIEF
This repo is created for sending the data of vehicles on the intersection od 120th street and Amsterdam Ave through MQTT. Then a MQTT-receiver gets the messages by subscribing the sender. The receiver will also call a sumo-gui, visualize and update the vehicles on the gui when receiving every message.

# FILES
There are three folders in this repo. 
- The folder *map* includes the sumo configures of the intersection. 

- The folder *py* contains the MQTT sender and receiver files and a python file to create the messages. 

- The folder *messages* contains the tracks of vehicles. The name of the file indicates the order of frame and the data format is type, id, heading_degree, speed, x, y

# Usage
To run the files, make sure you set the SUMO-HOME into your computers' PATH. Moreover, install 'traci' in python.

The receiver is designed to be used together with ns3. If you want to run sumo alone, change '--num-clients' , '2' to '--num-clients' , '1' in MQTTReceiver.py.

In order to run receive all messages. Run receiver then sender.
