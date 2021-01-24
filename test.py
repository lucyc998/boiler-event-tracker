import radarAPIcalls as r

#results = r.getNearestLocation("walc")
results = r.getAddresses("Walc")
print(results[0]['placeLabel'])