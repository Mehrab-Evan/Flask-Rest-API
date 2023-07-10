# Running the APis from seperate script files
import requests

SERVER_RUNNING_IN = "http://127.0.0.1:5000/"

response = requests.get(SERVER_RUNNING_IN + "/")

print(response.json())