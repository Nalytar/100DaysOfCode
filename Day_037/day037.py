# udemy Course - 100 Days of Code - Python

import json
import datetime
import requests

pixela_endpoint_user = "https://pixe.la/v1/users"
pixela_endpoint_graph = "https://pixe.la/v1/users/nalytar/graphs"
pixela_endpoint_graphid = "https://pixe.la/v1/users/nalytar/graphs/graph1"
pixela_endpoint_update = "https://pixe.la/v1/users/nalytar/graphs/graph1/20231231"
user_params = {}

with open("data.json", "r") as data:
	json_data = json.load(data)

	for endpoint_type, needed_data in json_data.items():
		user_params[endpoint_type] = needed_data
	user_params["GRAPH_ID"]["date"] = datetime.datetime.now().strftime("%Y%m%d")

	print(user_params)

# Creating a User
# response = requests.post(url=pixela_endpoint, json=user_params["USER_CREATE"])
# print(response.text)

# Creating a graph
# response = requests.post(url=pixela_endpoint_graph,
#                          json=user_params["GRAPH_CREATE"],
#                          headers=user_params["headers"])
# print(response.text)

# Creating a new Pixel on graph
# response = requests.post(url=pixela_endpoint_graphid,
#                          json=user_params["GRAPH_ID"],
#                          headers=user_params["headers"])
# print(response.text)

# Update a Pixel
# response = requests.put(url=pixela_endpoint_update,
#                         json={"quantity": "5"},
#                         headers=user_params["headers"])
# print(response.text)

# Delete a Pixel
# response = requests.delete(url=pixela_endpoint_update,
#                            headers=user_params["headers"])
# print(response.text)
