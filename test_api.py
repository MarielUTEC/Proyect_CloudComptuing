from flask import jsonify
import requests
import json 	
import requests
from test_api_2 import lista_url

lista_info = []
url = "https://youtube138.p.rapidapi.com/video/details/"



headers = {
	"X-RapidAPI-Key": "2f205d967cmshffde6f247a6d5cap12aec9jsn1ac72dd8e0db",
	"X-RapidAPI-Host": "youtube138.p.rapidapi.com"
}

for codigos in lista_url:
	lista_info_video = []

	querystring = {"id":codigos}

	response = requests.request("GET", url, headers=headers, params=querystring)
	
	response_json = response.json()

	lista_info_video.append(response_json["stats"])

	lista_info.append(lista_info_video)
	print(lista_info_video)


json_dump = json.dumps(lista_info_video)

with open('data.json', 'w') as file:
    json.dump(json_dump, file, indent=4)


