import requests

#scoring_url = 'https://ibm-watson-ml.mybluemix.net/v3/wml_instances/e43f71e5-f451-4b26-8476-2c42e336d67e/published_models/f8bf12c8-7cac-4e93-bcc6-86f3491f15d1/deployments/54b60ef1-b202-498b-8cec-0bc28ad35e13/online'
scoring_url = 'https://ibm-watson-ml.mybluemix.net/v3/wml_instances/e43f71e5-f451-4b26-8476-2c42e336d67e/published_models/7d18e7a5-3d13-4122-bc67-0e6e7404feb0/deployments/ee972fb1-e650-4669-9fe0-caae5693e787/online'
#payload_scoring = {"fields": ['temp','wspd','roof','surface','home','stadium_city','away_team','name','position','teamid'],
#					"values": [[60,10,"Open","Voyager Bermuda Grass",True,'Bank of America Stadium','ARI','J.Stewart','QB','CAR']]}
payload_scoring = {'fields': ['temp','wspd','roof','surface','ishome','stadium_city','away_team','name','position','teamid'],
					'values': [[60,10,'Open','Voyager Bermuda Grass',1,'Glendale, AZ','ARI','J.Stewart','QB','CAR']]}


import urllib3, requests, json

service_path = 'https://ibm-watson-ml.mybluemix.net'
instance_id = 'e43f71e5-f451-4b26-8476-2c42e336d67e'
username = '7efdfbec-da70-43cf-b4ce-3332be17d48d'
password = '37e5c543-837f-4f90-a854-1a388b62b27d'

headers = urllib3.util.make_headers(basic_auth='{}:{}'.format(username, password))
url = '{}/v3/identity/token'.format(service_path)

response = requests.get(url, headers=headers)
mltoken = json.loads(response.text).get('token')

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

#jsonPayload = json.dumps(payload_scoring)
#jsonPayload = json.loads(jsonPayload)
#print type(jsonPayload)
response_scoring = requests.post(scoring_url, json=payload_scoring, headers=header)

print response_scoring.text