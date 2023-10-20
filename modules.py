#import utility    # one way to call a module
#utility.find_max()



from utility import find_max   #second way to call module
numbers = [2,8,75,3,50,1]
maximus=find_max(numbers)
print(maximus)



from urllib.parse import urlparse

def valores_url(url: str) -> list:
    
    parametros = urlparse(url)[4].split("&")
    return [parametro.split("=")[1] for parametro in parametros]

#Prueba
print(valores_url("https://retosdeprogramacion.com?year=2023&challenge=0&age=30"))



from datetime import date

def is_fraiday_13(year:int,month:int):

   if date.isoweekday(date(year,month,1)) == 7:
      return True
   else: return False


print(is_fraiday_13(2023,10))
