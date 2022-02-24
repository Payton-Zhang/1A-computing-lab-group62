
from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import build_station_list, update_water_levels


def run():
    '''requirements for task 2B'''

    tol= 0.8 #tolerance 

    # Build list of stations and update level data
    stations = build_station_list()
    update_water_levels(stations)

    staions_above_tolerance=stations_level_over_threshold(stations, tol)

    for i in staions_above_tolerance:
        station=i[0]
        print(station.name, i[1])





if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    print('\n these are the stations with water over the treshhold of 0.8 \n')
    run()
