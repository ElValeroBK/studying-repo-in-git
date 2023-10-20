import requests
import json

# url= "https://api.artic.edu/api/v1/artworks?limit=3"
# url1="https://www.google.com/"
# reques = requests.get(url1)
# print(reques)

# if reques.status_code == 200:
#   #print(reques.content)
#   reques_json = reques.json()["data"]
#   for art in reques_json:
#      print(f"{art['id']} {art['api_link']} ")

# else: print("estatus_couse != 200")



# file = open("google.com",'wb')
# file.write(reques.content)
# file.close()

#-------------------
# def howmany_pokemon(url="https://pokeapi.co/api/v2/pokemon", offset: int = 0  , limit: int = 20):
    
#     arg = {'offset': offset ,'limit': limit}
#     respose = requests.get(url,params= arg)
#     peyload = respose.json()['results']
   
#     for pokemon in peyload:
#       print(pokemon)
    
#     next_offset  = input("desea ver proxima pagian (Y/N)").lower()

#     if next_offset == "y":
#        howmany_pokemon(offset=offset+20)

#     elif next_offset == "n":
#        print("fin de la busqeuda")

#     else: print("Error en la entrada")       

# howmany_pokemon()


#-----------------


### pendiente
# url = "https://api.github.com"

# session = requests.session()
# session.auth = ('willito85@gmail.com','Sitioty85githubbk')
# response = session.get(url)
# if response.ok:
#     print(response.json())

# else: print(response.status_code)





##api with python with oauth##

# client_id = "ba068cc927b8e9b58667"
# client_secrets = "2ec3a0142c8019397638d519d3aef3c63fe8a71a"
# url = "https://github.com/login/oauth/access_token"
# code = "be9069c0d4889bc4dd67"
# header={'Accept': 'application/json'}
# load = {'client_id':client_id,'client_secret':client_secrets,'code':code}
# # https://github.com/login/oauth/authorize?client_id=ba068cc927b8e9b58667&scope=repo
# access_token_valor = "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"


# response = requests.post(url, json=load, headers=header)

# if response.status_code== 200:
#     respnse_json = response.json()
#     access_token = respnse_json["token_type"]
#     print(access_token)
    

# url_2 = "https://github.com/api/v3/user"

# # "Authorization: Bearer OAUTH-TOKEN"

# response_2 = requests.post(url, json=load, headers=header)



# def parameter(url):
#      return list(i.split('=')[1]  for i in url.split('?')[1].split('&'))


# print (parameter("https://retosdeprogramacion.com?year=2023&challenge=casa&offset=2&client_id=55&limit=2034"))

