
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


# # Es un numero primo? ##

# def is_prime(num:int):
#     if num <= 1:
#        return False
#     for index in range(2,num):
#         if num % index == 0:
#             return False
#     return True

# def these_are_primes(cant):
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

def tenis_play(secuencia:list) -> list: # it saves the impression of the winner and the loser per line
    result = []
    p1=0
    p2=0  
    for secue in secuencia :        
        points_dir= {0:'Love',1:15,2:30,3:40,4:'Deuce',5:'Ventaja',6:'Ha ganado el'}
        if secue == "P1":  # (Player 1)
            p1+=1
            if (p2+2 == p1 and p2>2) or (p1==p2+4) or (p1==p2+3 and p2!=0) or (p1==p2+2 and p2!=1 and p2!=0): # winner
                result.append(f'{points_dir[6]} P1')
                break            
            elif p1==p2 and p1>2:                          
               result.append(f'{points_dir[4]}') # tied
            elif p1 == p2+1 and p1>3:             
               result.append(f'{points_dir[5]} P1') # forward
            else:                
               result.append(f'{points_dir[p1]} - {points_dir[p2]}') #regular score
        else: # (Player 2)
           p2+=1           
           if (p1+2 == p2 and p1>2) or (p2==p1+4) or (p2==p1+3 and p1!=0) or (p2==p1+2 and p1!=1 and p1!=0)  : #ganador
               result.append(f'{points_dir[6]} P2')
               break
           elif p1==p2 and p2>2:
              result.append(f'{points_dir[4]}') # tied
           elif p1+1 == p2 and p2>3:
              result.append(f'{points_dir[5]} P2') #forward
           else: 
              result.append(f'{points_dir[p1]} - {points_dir[p2]}') #regular score
  
    return result
  

def printresul(result:list)-> str: #imprime cada set ganado
    for a_favor in result:
        print(a_favor) 

secuencia = ['P1', 'P1', 'P2', 'P1', 'P2','P1']
printresul(tenis_play(secuencia))
