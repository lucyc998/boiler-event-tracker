import requests
import json


def getNearestLocation(buildingName):
    # coordinates for Purdue University
    coords = '40.423538,-86.9217'
    restParams = {'query': buildingName, 'near': coords}
    authHeader = {'Authorization': 'prj_test_pk_52f1b430dab9397c36c08527cf7957bbdf4bd9e6'}
    radarResponse = requests.get('https://api.radar.io/v1/search/autocomplete', headers=authHeader, params=restParams)
    return radarResponse


if __name__ == "__main__":
    userBuilding = input("Enter a building name: ")
    response = getNearestLocation(userBuilding)
    if response.status_code != 200:
        print("Error! Something went wrong!")
    else:
        locList = response.json()['addresses']
        for loc in locList:
            if 'placeLabel' in loc.keys():
                print(f"The address for \"{userBuilding}\" is at {loc['formattedAddress']}, it is also known as: {loc['placeLabel']}.")
            else:
                print(f"The address for \"{userBuilding}\" is at {loc['formattedAddress']}, We couldn't quite find a label for it though!")
            print(f"It is located at a latitude of {loc['latitude']} and a longitude of {loc['longitude']}.\n")