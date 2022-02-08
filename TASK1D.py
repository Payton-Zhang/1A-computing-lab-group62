from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation
from floodsystem.geo import rivers_with_station, stations_by_river

def run():
    stations = build_station_list()

    rivers = rivers_with_station(stations)

    rivers.sort()
    print("{} stations".format(len(rivers)))
    print("First 10: {}\n".format(rivers[:10]))

    river_info = stations_by_river(stations)
    for river in ["River Aire", "River Cam", "River Thames"]:
        names = []
        for item in river_info[river]:
            names.append(item.name)
        names.sort()

        print("Stations by {} :{}".format(river, names))
        print(" ")

    





if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
run()


