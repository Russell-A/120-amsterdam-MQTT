import traci

def AddVehicle(VehID, speed:float, position, typeID):
    # print("Add VehID",VehID, "position", position)

    if typeID == "car":
        typeID = "DEFAULT_VEHTYPE"
        traci.vehicle.add(vehID=VehID, routeID='', typeID = typeID , depart="now")
        traci.vehicle.moveToXY(vehID=VehID, edgeID="", lane = "0", x = position[0], y = position[1], keepRoute=0)
        traci.vehicle.setSpeed(vehID=VehID, speed=speed)
    elif typeID == "truck_bus":
        typeID = "DEFAULT_VEHTYPE"
    elif typeID == "bicycle":
        typeID = "DEFAULT_BIKETYPE"
    elif typeID == "person":
        typeID = "DEFAULT_PEDTYPE"
        edges = traci.edge.getIDList()
        traci.person.add(VehID, edgeID=edges[0], typeID = typeID, pos= 0)
        traci.person.moveToXY(VehID, edgeID="", x = position[0], y = position[1], keepRoute=0)
        traci.person.setSpeed(VehID, speed=speed)
        traci.person.setWidth(VehID, 1)
        traci.person.setLength(VehID, 1)
        traci.person.setColor(VehID, (255,255,0,255))





def RemoveVehicle(VehID, typeID):
    if typeID == "person":
        traci.person.remove(VehID)
    else:
        traci.vehicle.remove(VehID)
    
    
def UpdateVehicle(VehID, speed, position, angle, typeID):
    if typeID == "person":
        traci.person.moveToXY(VehID, edgeID="", x = position[0], y = position[1], keepRoute=0, angle = angle)
        traci.person.setSpeed(VehID, speed=speed)
    else:
        traci.vehicle.moveToXY(vehID=VehID, edgeID="", lane = "0", x = position[0], y = position[1], keepRoute=0, angle = angle)
        traci.vehicle.setSpeed(vehID=VehID, speed=speed)