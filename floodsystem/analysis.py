""""
This funtion returns an offset and an equation for the best fit line of the water level
"""

import matplotlib.pyplot as plt
import matplotlib.dates
import numpy
def polyfit(dates, levels, p):
    datenum = matplotlib.dates.date2num(dates)
    d0=datenum[0]
    p_coeff = numpy.polyfit(datenum - d0, levels, p)
    poly = numpy.poly1d(p_coeff)

    return(d0, poly)
