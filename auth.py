# import requests module
import requests
from requests.auth import HTTPBasicAuth

# Making a get request
response = requests.get('https://portal2.idtbrasilhosted.com/ / user, ',
			auth = HTTPBasicAuth('062099137', 'fabio.2626'))

# print request object
print(response)
