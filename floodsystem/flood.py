''' this module contains functions needed to access flood risks'''


# this function checks if current water level is over the threshold
def stations_level_over_threshold(stations, tol):
    list_of_stations= []
    for station in stations:
      water_level=  station.relative_water_level()
      if water_level != None:
        if water_level>= tol:
           s= (station, water_level)
           list_of_stations.append(s)
    list_of_stations.sort(reverse=True ,key=lambda a: a[1])
    return list_of_stations

# needed for 2c. Returns N stations with highest relative level
def stations_highest_rel_level(stations, N):
  list_of_stations = []
  for station in stations:
    water_level=  station.relative_water_level()
    if water_level != None:
      s= (station, water_level)
      list_of_stations.append(s)
  list_of_stations.sort(reverse=True ,key=lambda a: a[1])
  #makes list of top N stations
  top_stations=[]
  c=0
  while c<N:
    top_stations.append(list_of_stations[c])
    c= c+1
  return top_stations

