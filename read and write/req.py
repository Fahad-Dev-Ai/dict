import requests
import json
response = requests.get("https://jsonplaceholder.typicode.com/users")
data = response.json()
print(data)
for user in data:
    users = []
    users.append({"name" : user["name"],"email" : user["email"]})
with open ("users.json","w") as f:
    json.dump(users,f)