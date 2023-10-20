'''for item in range(10):
    print(item)
'''
total = 0
for artic in [10,20,30]:
   total +=artic
print (total) 


amount_x = [5,2,5,2,2]

for x in amount_x:
     strings = ''
     for lines in range(x):
         strings += 'x'
     print(strings)

          
from urllib.parse import urlparse

def valores_url(url: str) -> list:
    
    parametros = urlparse(url)[4].split("&")
    print(parametros)
    
    return [parametro.split("=")[1] for parametro in parametros]
 
#Prueba
print(valores_url("https://retosdeprogramacion.com?year=2023&challenge=0"))




def all_parameter(url:str)->list:


    split = url.split("?")
    splited=split[1].split("=")
    momentaneo=[]
    string=""
    result=[]

    
    for x in splited[1:-1]:
        momentaneo.clear()
        for value in x:
            if value!="&":
                momentaneo.append(value)
            else: 
                string= "".join(momentaneo)
                result.append(string)
                break
    result.append(splited[-1])
    print(result)  
            
all_parameter("https://retosdeprogramacion.com?year=2023&challenge=casa&offset=2&client_id=55&limit=2034")



 


