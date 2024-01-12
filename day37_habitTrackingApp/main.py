import requests
from datetime import datetime

# ----------------------------------------- CREATE OUR PROFILE IN PIXE.LA -----------------------------------------
pixela_endpoint = "https://pixe.la/v1/users"
# user token,user name, graphid  is chosen by us
USER_TOKEN = "hefjeic65344tgefved"
USER_NAME = "hue"
user_parameters = {
    "token": USER_TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
GRAPH_ID = "graph16"

# use this post 1 times to create new post profile for unexisting profile, then delete
# response=requests.post(url=pixela_endpoint, json=user_parameters)
# print(response.text)


# ---------------------------------------------- CREATE GRAPH----------------------------------------------
graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"
headers = {
    "X-USER-TOKEN": USER_TOKEN
}
graph_params = {
    "id": GRAPH_ID,
    "name": "eat tracking",
    "unit": "calories",
    "type": "float",
    "color": "shibafu",
}

# use these 2 steps to create first unexisting graph, then delete when the graph sucessfully created
# graph_response=requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(graph_response.text)


# ---------------------------------------------- POST PIXEL, NEW VALUE ----------------------------------------------
today = datetime.now().strftime("%Y%m%d")
print(today)
pixel_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}"
pixel_config = {
    "date": today,
    "quantity": "9.5"
}

# use this to add new value
# pixel_response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
# check picel rsponse
# print(pixel_response.text)


# ---------------------------------------------- UPDATE PIXEL, VALUE----------------------------------------------
pixel_update_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{today}"
pixel_update_config = {
    "quantity": "7.5"
}
# pixel_update_response = requests.put(url=pixel_update_endpoint, json=pixel_update_config, headers=headers)
# print(pixel_update_response.text)

# ---------------------------------------------- DELETE PIXEL, VALUE----------------------------------------------

delete_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{today}"
# delete_response = requests.delete(url=delete_endpoint, headers=headers)
# print(delete_response)
