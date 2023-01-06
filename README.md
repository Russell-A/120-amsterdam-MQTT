# 120-amsterdam-mqtt (Python)

## BRIEF
This repo is created for sending the data of vehicles on the intersection od 120th street and Amsterdam Ave through MQTT. Then a MQTT-receiver gets the messages by subscribing the sender. The receiver will also call a sumo-gui, visualize and update the vehicles on the gui when receiving every message.

## FILES
There are three folders in this repo. 
- The folder *map* includes the sumo configures of the intersection. 

- The folder *py* contains the MQTT sender and receiver files and a python file to create the messages. 

- The folder *messages* contains the tracks of vehicles. The name of the file indicates the order of frame and the data format is type, id, heading_degree, speed, x, y

- The folder *messages-with-pedestrains* contains the tracks of vehicles. The name of the file indicates the order of frame and the data format is type, id, heading_degree, speed, x, y. It's linked with map1

- The folder *messages-latest* contains the tracks of vehicles. The name of the file indicates the order of frame and the data format is type, id, heading_degree, speed, x, y. It's linked with map-latest


## Usage
To run the files, make sure you set the SUMO-HOME into your computers' PATH. Moreover, install 'traci' in python.

The receiver is designed to be used together with ns3. If you want to run sumo alone, change '--num-clients' , '2' to '--num-clients' , '1' in MQTTReceiver.py.

In order to run receive all messages. Run receiver then sender.


## Details
### MQTT
![](https://mqtt.org/assets/img/mqtt-publish-subscribe.png)

The MQTT sender will read the data in folder 'messages' one by one. After reading a file, which includes all the vehicle information needed for simulation in one frame. The MQTT sender will send the data to the server. And the receive then can subscibe and retrieve the information in string format.

The receiver will first call a Sumo-Gui and initial the network information. Then when it recieves a message, it will decode it first. Then it will update the vehicle infomation in sumo according to the data. The update includes adding or removing a vehicle, update a vehicle's speed, heading and position.
