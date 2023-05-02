import requests
import json

url = "https://youtube138.p.rapidapi.com/playlist/videos/"

querystring = {"id":"PLp22EiLpMLDdvp6C4W2plwhyoAF-pXASA"}

headers = {
	"X-RapidAPI-Key": "2f205d967cmshffde6f247a6d5cap12aec9jsn1ac72dd8e0db",
	"X-RapidAPI-Host": "youtube138.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)




response_json = response.json()

lista_url = []
for i in range(len(response_json["contents"])):
    lista_url.append(response_json["contents"][i]["video"]["videoId"])

#print(lista_url)





with open('api2.json', 'w') as file:
    json.dump(response_json, file, indent=4)

