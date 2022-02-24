from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels

def run():
    '''requirements for task 2C'''

    stations = build_station_list()
    update_water_levels(stations)

    print('\n these are the ten stations with the highest relative water level\n')
    stations_list= stations_highest_rel_level(stations,10)
    for i in stations_list:
        station= i[0]
        print(station.name, i[1])
    


if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")
    run()