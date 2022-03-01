from floodsystem.plot import plot_water_level_with_fit
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
import matplotlib.pyplot as plt
import datetime
from floodsystem.flood import stations_highest_rel_level

stations = build_station_list()
update_water_levels(stations)
stations = stations_highest_rel_level(stations, 6)

for station in stations:
    dates, levels = fetch_measure_levels(station[0].measure_id, dt=datetime.timedelta(days=2))
    if not dates:
        print(station[0].name)
        pass
    else:
        print(dates)
        plot_water_level_with_fit(station[0], dates, levels, 4)
        plt.show()