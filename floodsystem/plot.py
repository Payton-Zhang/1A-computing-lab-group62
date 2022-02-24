import matplotlib.pyplot as plt
import matplotlib.dates
from datetime import datetime, timedelta
from floodsystem.analysis import polyfit
import floodsystem
import numpy
def plot_water_levels(station, dates, levels):
    print("test")
    plt.plot(dates, levels)
    plt.axhline(y=station.typical_range[0])
    plt.axhline(y=station.typical_range[1])
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title("Station " + station.name)
    plt.tight_layout()  # This makes sure plot does not cut off date labels


def plot_water_level_with_fit(station, dates, levels, p):
    plot_water_levels(station, dates, levels)
    d0, poly = polyfit(dates, levels, p)
    datenum = matplotlib.dates.date2num(dates)
    leveladj = poly(datenum-d0)
    plt.plot(datenum, leveladj, '.')
"""
    x1 = numpy.linspace(x[0], x[-1], 30)
    plt.plot(x1, poly(x1 - x[0]))
"""
