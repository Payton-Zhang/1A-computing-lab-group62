import matplotlib.pyplot as plt
import matplotlib.dates
import numpy
def polyfit(dates, levels, p):
    datenum = matplotlib.dates.date2num(dates)
    print(dates)
    print(datenum)
    d0=datenum[0]
    p_coeff = numpy.polyfit(datenum - d0, levels, p)
    poly = numpy.poly1d(p_coeff)

    return(d0, poly)
