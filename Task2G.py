import matplotlib.pyplot as plt
import matplotlib.dates
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
import datetime
from floodsystem.analysis import polyfit
from floodsystem.flood import stations_highest_rel_level
from floodsystem.plot import plot_water_level_with_fit


stations = build_station_list()
print (len(stations))
update_water_levels(stations)
stations = stations_highest_rel_level(stations, 50)
high= []
mid = []
low = []
no = []

for station in stations:
    dates, levels = fetch_measure_levels(station[0].measure_id, dt=datetime.timedelta(days=2))
    if not dates:
        pass
    else:
        d0, poly = polyfit(dates, levels, 13)
        datenum = matplotlib.dates.date2num(dates)
        leveladj = poly(datenum-d0)
        grad = 0

        for i in range(5):
            grad += (leveladj[i+7]-leveladj[i+12])/(datenum[i+7]-datenum[i+12])
        grad /= 5
        print(grad)
        if grad>0.5 and grad<=1:
            mid.append(station[0].name)
            print(grad)
        elif grad > 1:
            print(station[0].name)
            high.append(station[0].name)
        elif grad<=0.5 and grad>0:
            low.append(station[0].name)
        elif grad<=0:
            no.append(station[0].name)
        print(station[0].name)
        plot_water_level_with_fit(station[0], dates, levels, 13)
        plt.show()
print("Done")
        

print(no,low,mid,high)
print(len(no)+len(low)+len(mid)+len(high))







