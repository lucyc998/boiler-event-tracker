import requests
import json

headers = {'Authorization' : 'prj_test_pk_52f1b430dab9397c36c08527cf7957bbdf4bd9e6'}
response = requests.get('https://api.radar.io/v1/search/autocomplete?query=corec&near=40.423538,-86.9217', headers=headers)
print(json.dumps(response.json(), indent=4))