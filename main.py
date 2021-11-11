import os
from datetime import datetime
import webbrowser
import requests

new = 2
username = os.environ["username"]
token = os.environ["token"]
user_params = {
    "token": token,
    "username": username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

pixela_endpoint = "https://pixe.la/v1/users"
response = requests.post(url=pixela_endpoint, json=user_params)
graph_endpoint = f"{pixela_endpoint}/{username}/graphs"
graph_config = {
    "id": "graph1",
    "name": "Productivity Graph",
    "unit": "hours",
    "type": "float",
    "color": "ichou"

}
headers = {
    "X-USER-TOKEN": token
}
response = requests.post(graph_endpoint, json=graph_config, headers=headers)
graphID = "graph1"
date = datetime.now().strftime('%Y%m%d')
pixel_config = {
    "date": date,
    "quantity": input("How Many Productive Hours Today? ")
}
graph_creation_endpoint = f"{pixela_endpoint}/{username}/graphs/{graphID}"
response = requests.post(graph_creation_endpoint, json=pixel_config, headers=headers)
if response.status_code == 200:
    webbrowser.open(graph_creation_endpoint, new=new)
