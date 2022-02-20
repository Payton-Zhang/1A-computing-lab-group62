from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list
from floodsystem.plot import plot_water_levels
import matplotlib.pyplot as plt
import datetime


stations = build_station_list()


update_water_levels(stations)
stations = stations_highest_rel_level(stations, 5)



for station in stations:
    if station.typical_range_consistent():
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=10))
        plot_water_levels(station, dates, levels)

