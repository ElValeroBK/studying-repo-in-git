
#    ## EL FAMOSO FIZZ BUZZ [Fácil] ##

# def rango():
#     for numero in range(1,101):

#      if numero % 3== 0 and numero % 5 == 0:
#         print("fizzbuzz")
    
#      if numero % 3 == 0:
#         print("fizz")
    
#      elif numero % 5 == 0:
#         print("buzz")

#      else:
#          print(numero)

# rango()


#     ## Es un anagrama?[Facil] ##


# def es_anagrama(word_one:str,wordtwo:str):
#     if word_one.lower() == wordtwo.lower():
#         return False
#     return sorted(word_one.lower()) == sorted(wordtwo.lower())
  

# print(es_anagrama("Hose","hose"))


# ## Sucesion de fibonacci [Facil] ##

# def fibonacci():
#     fibona_list = [0,1]
#     for iter in range(48):
#         fibona_list.extend([fibona_list[-1] + fibona_list[-2]]) 
        
#     print(fibona_list)

# # fibonacci()


# Es un numero primo? ##

# def is_prime(num:int):
#     if num <= 1:
#        return False
#     for index in range(2,num):
#         if num % index == 0:
#             return False
#     return True

# def these_are_primes(cant):
#     primo_list = list
#     for index in range(2,cant+1):
#         if is_prime(index):
#             print(index)
           

# these_are_primes(100)



# ### Invirtiendo candenas ### first way ##

# def reversing_chains(text):
#     revers_text = list(text)
#     correct_text =""
#     i=1
#     for index in text:
#       revers_text [len(text)-i] = index
#       i+=1
      
    
#     for i in revers_text:
#        correct_text+= i

    

#     return correct_text
   

# print(reversing_chains("Hola mundo"))

# ### Invirtiendo candenas ### second way ##

# def reversing_chains(text):
#     revers_text = ''
#     for index in range(0, len(text)):
#         revers_text+= text[len(text) - index -1]
    
#     return revers_text

# print(reversing_chains("Hola mundo"))


## EL PARTIDO DE TENIS ##

#  * Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
#  * El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
#  * gane cada punto del juego.
#  * 
#  * - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
#  * - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
#  *   15 - Love
#  *   30 - Love
#  *   30 - 15
#  *   30 - 30
#  *   40 - 30
#  *   Deuce
#  *   Ventaja P1
#  *   Ha ganado el P1
#  * - Si quieres, puedes controlar errores en la entrada de datos.   
#  * - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos. 

# def tenis_play(secuencia:list) -> list: # it saves the impression of the winner and the loser per line
#     result = []
#     p1=0
#     p2=0  
#     for secue in secuencia :        
#         points_dir= {0:'Love',1:15,2:30,3:40,4:'Deuce',5:'Ventaja',6:'Ha ganado el'}
#         if secue == "P1":  # (Player 1)
#             p1+=1
#             if (p2+2 == p1 and p2>2) or (p1==p2+4) or (p1==p2+3 and p2!=0) or (p1==p2+2 and p2!=1 and p2!=0): # winner
#                 result.append(f'{points_dir[6]} P1')
#                 break            
#             elif p1==p2 and p1>2:                          
#                result.append(f'{points_dir[4]}') # tied
#             elif p1 == p2+1 and p1>3:             
#                result.append(f'{points_dir[5]} P1') # forward
#             else:                
#                result.append(f'{points_dir[p1]} - {points_dir[p2]}') #regular score
#         else: # (Player 2)
#            p2+=1           
#            if (p1+2 == p2 and p1>2) or (p2==p1+4) or (p2==p1+3 and p1!=0) or (p2==p1+2 and p1!=1 and p1!=0)  : #ganador
#                result.append(f'{points_dir[6]} P2')
#                break
#            elif p1==p2 and p2>2:
#               result.append(f'{points_dir[4]}') # tied
#            elif p1+1 == p2 and p2>3:
#               result.append(f'{points_dir[5]} P2') #forward
#            else: 
#               result.append(f'{points_dir[p1]} - {points_dir[p2]}') #regular score
  
#     return result
  

# def printresul(result:list)-> str: #imprime cada set ganado
#     for a_favor in result:
#         print(a_favor) 

# secuencia = ['P1', 'P1', 'P2', 'P1', 'P2','P1']
# printresul(tenis_play(secuencia))



## Reto #9: Heterograma, isograma y pangrama

# #01 Heterograma
# #mio
# def heterograma(word:str)->str:      
#    for i in range(len(word)-1):
#       if len((list(filter(lambda item: word[i+1]==item,word)))) >= 2 :
#          return(word + " : No es un Heterograma")
#    return(word+": Es un Heterograma")

# print(heterograma("asdfghz"))


##de alguien mas
# def heterograma2(word:str)->bool: 
#    for i in word:
#        if word.count(i)!=1:         
#          return True  
                    
#    return False

# print(heterograma2("aasdfghz"))


##2 isograma

# def isograma (word:str)->bool:
#    cont =dict()
#    for chart in word:
#       if chart in cont.keys():
#          cont[chart] += 1
#       else:
#          cont[chart] = 1
#    for values in list(cont.values()):
#       if values!=2:
#          return False
#    return True
      

# print(isograma("lolocasacs"))


##3 Pangrama 
# def is_pangrama(word:str)->bool:
#    const =["q","w","e","r","t","y","u",'i','o','p','a','s','d',
#            'f','g','h','j','k','l','z','x','c','v','b','n','m'," "]
#    comprueve=dict.fromkeys(const)
#    for chart in word:
#       if comprueve[chart] == None:
#          comprueve[chart]=1
#       else: comprueve[chart]+=1

#    for chart in list(comprueve.values()):
#       if chart == None:
#          return False
#    return True


# print(is_pangrama("el veloz mjurcielago hindu comia feliz cardillo y kiwi la ciguena tocaba el saxofon detras del palenque de paja"))



#Reto: #3  EL GENERADOR DE CONTRASEÑAS [Media]

# # Importamos el método sample de random.
# from random import sample
# import string

# # Declaramos la función con un argumento (longitud de la contraseña)
# def password_generator(longitud):
#     if longitud>= 8 and longitud<= 16:

#         # Definimos los caracteres simbolos y numeros
#         abc =""
#         abc = string.ascii_letters 
#         numeros = ""
#         numeros = string.digits
#         simbolos= ""
#         simbolos = string.punctuation
        
#         # Definimos la secuencia
#         secuencia = abc + numeros + simbolos
        
#         # Llamamos la función sample() utilizando la secuencia, y la longitud
#         password_union = sample(secuencia, longitud)
        
#         # Con join insertamos los elementos de una lista en una cadena
#         password_result = "".join(password_union)
        
#         # Retornamos la variables "password_result"
#         return password_result

#     respuesta = "la longitud de los caracteres deve tener entre 8 y 16"
#     return respuesta

# # Llamos a la función "password_generatos" y le pasamos el valor "12" 
# password = password_generator(16)

# # Imprimimos el resultado
# print("Contraseña: ", password)



#Reto #4: PRIMO, FIBONACCI Y PAR
# def is_fibonacci_num(number:int)-> int:  #Returns the number of the Fibonacci sequence. 
#     if number == 0:
#         return 0
#     elif number == 1:
#         return 1
#     else: 
#         return is_fibonacci_num(number-2) + is_fibonacci_num(number-1)

# def is_primo(number): # retunr true or falce if the number is Primo
#    if number == 2:
#       return True

#    if number % 2 == 0:
#       return False
#    else: return True


# def is_fibonacci(number:int)->bool: # retunr true or falce if the number is fibonacci
#    fibo_list =[1,1] 

#    while fibo_list[-1] < number:
#       fibo_list.append(fibo_list[-2] + fibo_list[-1])
         
#    if fibo_list[-1] == number:
#       return True
#    else: return False
   

# def is_par(number):
#     if number % 2 == 0:
#        return True
#     else: return False

# def is_primo_fibonacci_par(number):
#     secuencia = str()
#     if is_primo(number):
#        secuencia = "es primo, "
#     else: secuencia = "no es primo, "
#     if is_fibonacci(number):
#        secuencia +="es fibonacci, "
#     else: secuencia += "no es fibonacci, "
#     if is_par(number):
#        secuencia += "y es par"
#     else: secuencia += "Y es inpar"
  
#     print(secuencia)
    

# print(is_primo(5))
# print(is_fibonacci(121393))
# print(is_par(10))

#is_primo_fibonacci_par(2)


# import time
# import math

# def number_pseudo():
#     tiempo_actual = time.time()
#     print(tiempo_actual)
#     valor, _ = math.modf(tiempo_actual)
#     var = valor * 1000

#     if int(var) == 100:
#         return 100
#     else:
#         return int(valor * 100)

# print(number_pseudo())

### Reto #11 - URL PARAMS  ###

#  Dada una URL con parámetros, crea una función que obtenga sus valores.
#  No se pueden usar operaciones del lenguaje que realicen esta tarea directamente.
 
#  Ejemplo: En la url https://retosdeprogramacion.com?year=2023&challenge=0
#  los parámetros serían ["2023", "0"]



# def all_parameter(url:str)->list:
#     split = url.split("?")
#     splited=split[1].split("=")
#     momentaneo=[]
#     string=""
#     result=[]

    
#     for x in splited[1:-1]:
#         momentaneo.clear()
#         for value in x:
#             if value!="&":
#                 momentaneo.append(value)
#             else: 
#                 string= "".join(momentaneo)
#                 result.append(string)
#                 break
#     result.append(splited[-1])
#     print(result)  
            
# all_parameter("https://retosdeprogramacion.com?year=2023&challenge=casa&offset=2&client_id=55&limit=2034")



# from datetime import date

# def is_fraiday_13():
#    print("ingresa el año y el mes para saber si contiene un viernes 13 ")
#    year,month = map(int,input().split())
   

#    if date.weekday(date(year,month,1)) == 6:
#       print (True)
#    else: print(False)


# is_fraiday_13()

### Reto #13: Adivina la palabra ###


from urllib.request import Request, urlopen
from random import  randrange
import numpy

def words_list(amount:int)->list:     # devuelve una lista de palabras con la cantidad celecionadas no mas de 25488 palabras
    url="https://svnweb.freebsd.org/csrg/share/dict/words?revision=61569&view=co"
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    web_byte = urlopen(req).read()
    webpage = web_byte.decode('utf-8')
    lista=str(webpage).split("\n") # 25488
    ram = randrange(50,25488-amount)
    return(lista[ram:ram+amount])

def word_random_choice(words:list)->str: # devuelve una palabra ramdom de una lista 
    return numpy.random.choice(words)

def hide_char_in_the_word(word:str)->int:  # devuelve una palabra con el 50% de la palabra oculta

    cont = len(word)

    
    return int(cont*0.50) 
    
