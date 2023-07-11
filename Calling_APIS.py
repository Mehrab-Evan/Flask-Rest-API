# import requests
#
# Server = "http://127.0.0.1:5000/"
#
# response = requests.put(Server + "task/1", {"topic":"Research and Development"})
# print(response.json())
# print("WHY NOTS WORKING")


# This Calling_API file is almost working as a postman api testing
import requests

Server = "http://127.0.0.1:5000/"

payload = {
    "topic": "Research and Development",
    "link": "https://example.com",
    "problem": "Some problem description"
}

response = requests.put(Server + "task/1", json=payload)
response2 = requests.get(Server + "task/1")
print(response2.json())
print(response.json())
