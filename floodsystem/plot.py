import matplotlib.pyplot as plt
import matplotlib.dates
from datetime import datetime, timedelta
from floodsystem.analysis import polyfit
import floodsystem
import numpy
#This funtion plots the typical high and low values for a given station, along with the historical water level over time
def plot_water_levels(station, dates, levels):
    plt.plot(dates, levels)
    plt.axhline(y=station.typical_range[0])
    plt.axhline(y=station.typical_range[1])
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title("Station " + station.name)
    plt.tight_layout()  # This makes sure plot does not cut off date labels


#This function adds a best fit line to the previous function of polynomial order 3

def plot_water_level_with_fit(station, dates, levels, p):
    plot_water_levels(station, dates, levels)
    d0, poly = polyfit(dates, levels, p)
    datenum = matplotlib.dates.date2num(dates)
    leveladj = poly(datenum-d0)
    plt.plot(datenum, leveladj, '.')

