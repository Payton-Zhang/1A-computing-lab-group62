import matplotlib
import numpy
def polyfit(dates, levels, p):
    datenum = matplotlib.dates.date2num(dates)
    y = levels
    p_coeff = numpy.polyfit(datenum, y, p)