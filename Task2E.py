from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.plot import plot_water_levels
import matplotlib.pyplot as plt
import datetime
from floodsystem.flood import stations_highest_rel_level


stations = build_station_list()


update_water_levels(stations)
stations = stations_highest_rel_level(stations, 5)
untuple = []
for i in range(len(stations)):
    untuple.append(stations[i][0])
stations = untuple

for station in stations:
    if station.typical_range_consistent():
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=10))
        plot_water_levels(station, dates, levels)
    plt.show()
