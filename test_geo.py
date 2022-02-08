from floodsystem.geo import stations_by_distance
from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list
import random
from haversine import haversine
from floodsystem.station import MonitoringStation

'''
Tests to see if all values are smaller than the next one in list
'''
def test_geo_list():
    stations = build_station_list()
    assert stations != None
    p = (random.randint(0,5), random.randint(0,5))
    assert p != None
    station_list=stations_by_distance(stations, p)
    for i in range (0, (len(station_list)-2)):
        stat1=station_list[i]
        stat2=station_list[i+1]
        stat1=stat1[1]
        stat2=stat2[1]
        assert stat1<=stat2

'''
Tests to see if station within radius is classed as within radius
'''

def test_geo_rad():
    coord1 = (9.9, 9.9)
    coord2 = (10,10)
    stat = "stat"
    measure = "measure"
    name = "label"
    trange = None
    river = "River"
    town = "Town"
    center = (0,0)

    s1 = MonitoringStation(stat, measure, name, coord1, trange,
                 river, town)
    s2 = MonitoringStation(stat, measure, name, coord2, trange,
                 river, town)
    stations=[s1,s2]
    rad = haversine(center, coord1)+1
    radius = stations_within_radius(stations, center, rad)
    assert len(radius) == 1
    assert radius[0][0] == s1

'''
Tests to see if both types of invalid range data is flagged as so
'''

def test_validity_valuation():
    coord1 = (9.9, 9.9)
    coord2 = (10,10)
    stat = "stat"
    measure = "measure"
    name = "label"
    trange1 = (10,9)
    trange2 = None
    river = "River"
    town = "Town"
    center = (0,0)

    s1 = MonitoringStation(stat, measure, name, coord1, trange1,
                 river, town)
    s2 = MonitoringStation(stat, measure, name, coord2, trange2,
                 river, town)
    stations=[s1,s2]

    assert s1.typical_range_consistent() == False
    assert s2.typical_range_consistent() == False





test_geo_list()
test_geo_rad()
test_validity_valuation()

def test_stations_by_distance():
    """ Test finding the distance between two points """
    point1 = (50.0359, 5.4253)
    point2 = (58.3838, 3.0412)

    distance = haversine(point1, point2)

    assert distance == 940.9489257526606

def test_station_within_radius():
    """ Test checking whether a point is within a radius of another point """
    cambridge = (52.2053, 0.1218)
    r = 500

    point1 = (50.0359, 5.4253)
    distance1 = haversine(cambridge, point1)
    if distance1 < r:
        within_radius = True
    else:
        within_radius = False
    assert within_radius == True

    point2 = (58.3838, 3.0412)
    distance2 = haversine(cambridge, point2)
    if distance2 < r:
        within_radius = True
    else:
        within_radius = False
    assert within_radius == False


def testing_rivers_by_station_number():
    """ Test to check can increase the number of a value of a dictionary """
    test_dict = {}
    test_list = [1, 4, 5, 45, 85, 88, 93, 99, 100]

    for number in test_list:
        if number % 2 == 0:
            if "even" in test_dict.keys():
                test_dict["even"] += 1
            else:
                test_dict["even"] = 1
        else:
            if "odd" in test_dict.keys():
                test_dict["odd"] += 1
            else:
                test_dict["odd"] = 1

    assert list(test_dict.keys()) == ["odd", "even"]
    assert list(test_dict.values()) == [6, 3]
