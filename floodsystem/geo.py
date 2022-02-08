
"""This module contains a collection of functions related to
geographical data.
"""

from ..utils import sorted_by_key  # noqa
from haversine import haversine

def stations_by_distance(stations, p):
    '''
    sorts the inputted stations by distance from given point p
    '''
    distances = []
    for station in stations:
        cdist = haversine(station.coord, p)
        distances.append((station, cdist))
    distances=sorted_by_key(distances, 1)
    return distances

def stations_within_radius(stations, centre, r):
    '''
    returns stations within certain radius of a given coordinate
    '''
    stat_list=stations_by_distance(stations, centre)
    stat_close=[]
    for station in stat_list:
        if station[1] < r:
            stat_close.append(station)
    return(stat_close)

def rivers_with_station(stations):
    rivers = []
    for station in stations:
        if station.river in rivers:
            pass
        else:
            rivers.append(station.river)
    
    return rivers


def stations_by_river(stations):

    stations_on_each_river = dict()

    for station in stations:
        if station.river in stations_on_each_river:
            stations_on_each_river[station.river].append(station)
        else:
            stations_on_each_river[station.river] = [station]
    return stations_on_each_river

def rivers_by_station_number(stations, N):
    rivers = dict()
    for station in stations:
        if station.river in rivers:
            rivers[station.river] += 1 
        else:
            rivers[station.river] = 1
    
    N_station = [] 
    for river in rivers:
        N_station.append((river, rivers[river]))
    
    N_station.sort(key=lambda a: a[1], reverse= True)

    N_station_N = N_station[:N]
   
    for i in range(len(stations)):
        if N_station[N-1][1] == N_station[N+i][1]:
            N_station_N.append(N_station[N+i])
        else:
            break

    return N_station_N