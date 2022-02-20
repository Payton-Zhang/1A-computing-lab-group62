import matplotlib.pyplot as plt
from datetime import datetime, timedelta
def plot_water_levels(station, dates, levels):
    print("test")
    plt.plot(dates, levels)
    plt.axhline(y=station.typical_range[0])
    plt.axhline(y=station.typical_range[1])
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title("Station ")
    plt.tight_layout()  # This makes sure plot does not cut off date labels
    plt.show()
