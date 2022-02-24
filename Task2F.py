from floodsystem.plot import plot_water_level_with_fit
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list
import matplotlib.pyplot as plt
import datetime


stations = build_station_list()
station = stations[6]


dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=2))

plot_water_level_with_fit(station, dates, levels, 4)
plt.show()

"""
for station in stations:
    if station.typical_range_consistent():
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=10))
        plot_water_level_with_fit(station, dates, levels, 4)
        plt.show
"""