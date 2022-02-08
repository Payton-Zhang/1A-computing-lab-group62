
from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance

stations = build_station_list()
list1 = stations_by_distance(stations, (52.2053, 0.1218))
finlist=[]

for station in list1:
    name=station[0].name
    town=station[0].town
    distance=station[1]
    finlist.append((name, town, distance))
trimlist = []
trimlist.append (finlist[:10])
trimlist.append (finlist[-10:])
print (trimlist)
