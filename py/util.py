import traci

def AddVehicle(VehID, speed:float, position, typeID):
    print("Add VehID",VehID, "position", position)

    if typeID == "car":
        typeID = "DEFAULT_VEHTYPE"
    elif typeID == "truck_bus":
        typeID = "DEFAULT_VEHTYPE"
    elif typeID == "bicycle":
        typeID = "DEFAULT_BIKETYPE"
    elif typeID == "pedestrian":
        typeID = "DEFAULT_PEDTYPE"


    traci.vehicle.add(vehID=VehID, routeID='', typeID = typeID , depart="now")
    traci.vehicle.moveToXY(vehID=VehID, edgeID="", lane = "0", x = position[0], y = position[1], keepRoute=2)
    traci.vehicle.setSpeed(vehID=VehID, speed=speed)

def RemoveVehicle(VehID):
    traci.vehicle.remove(VehID)
    
def UpdateVehicle(VehID, speed, position, angle):
    traci.vehicle.moveToXY(vehID=VehID, edgeID="", lane = "0", x = position[0], y = position[1], keepRoute=2, angle = angle)
    traci.vehicle.setSpeed(vehID=VehID, speed=speed)