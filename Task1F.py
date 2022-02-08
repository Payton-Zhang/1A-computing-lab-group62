from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations
stations = build_station_list()
incon_station=inconsistent_typical_range_stations(stations)
incon_names=[]
for station in incon_station:
    incon_names.append(station.name)
incon_names.sort()
print (incon_names)
