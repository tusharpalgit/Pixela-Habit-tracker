from datetime import datetime
import requests

USERNAME="tusharpal"
TOKEN="ambica@123"
GRAPHID="graph1"

pixela_endpoint="https://pixe.la/v1/users"

user_params={
    "token":TOKEN,
"username":USERNAME,
"agreeTermsOfService":"yes",
    "notMinor":"yes"
}

#<------------------------To Create a new user------------------>
# response=requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

#link for page= https://pixe.la/@tusharpal

graph_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config={
    "id":GRAPHID,
"name":"Workout Graph",
"unit":"km",
"type":"float",
"color":"ichou"
}
authorise={
    "X-USER-TOKEN":TOKEN
}

#<------------------To create new graph------------------------------>
# response=requests.post(url=graph_endpoint,json=graph_config,headers=authorise)
# print(response.text)

pixel_creation_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}"
today=datetime.now()
pixel_data={
    "date":today.strftime("%Y%m%d"),
"quantity":"15"
}
#<---------------------------------post pixel data----------------------------->
# response=requests.post(url=pixel_creation_endpoint,json=pixel_data,headers=authorise)
# print(response.text)

update_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/{today.strftime('%Y%m%d')}"

new_pixel_data={
    "quantity":"4.5"
}
#<-----------------------------TO update pixel data-------------------------------------------->
# response=requests.put(url=update_endpoint, json=new_pixel_data, headers=authorise)
# print(response.text)

delete_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/{today.strftime('%Y%m%d')}"

#<---------------------TO delete pixel data-------------------------->
# response=requests.delete(url=delete_endpoint,headers=authorise)
# print(response.text)