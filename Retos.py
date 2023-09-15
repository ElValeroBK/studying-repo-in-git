
   ## EL FAMOSO FIZZ BUZZ [Fácil] ##

def rango():
    for numero in range(1,101):

     if numero % 3== 0 and numero % 5 == 0:
        print("fizzbuzz")
    
     if numero % 3 == 0:
        print("fizz")
    
     elif numero % 5 == 0:
        print("buzz")

     else:
         print(numero)

rango()


    ## Es un anagrama?[Facil] ##


def es_anagrama(word_one:str,wordtwo:str):
    if word_one.lower() == wordtwo.lower():
        return False
    return sorted(word_one.lower()) == sorted(wordtwo.lower())
  

print(es_anagrama("Hose","hose"))


## Sucesion de fibonacci [Facil] ##

def fibonacci():
    fibona_list = [0,1]
    for iter in range(48):
        fibona_list.extend([fibona_list[-1] + fibona_list[-2]]) 
        
    print(fibona_list)

# fibonacci()


# Es un numero primo? ##

def is_prime(num:int):
    if num <= 1:
       return False
    for index in range(2,num):
        if num % index == 0:
            return False
    return True

def these_are_primes(cant):
    for index in range(2,cant+1):
        if is_prime(index):
            print(index)
           

these_are_primes(100)


### Invirtiendo candenas ### first way ##

def reversing_chains(text):
    revers_text = list(text)
    correct_text =""
    i=1
    for index in text:
      revers_text [len(text)-i] = index
      i+=1
      
    
    for i in revers_text:
       correct_text+= i

    

    return correct_text
   

print(reversing_chains("Hola mundo"))

### Invirtiendo candenas ### second way ##

def reversing_chains(text):
    revers_text = ''
    for index in range(0, len(text)):
        revers_text+= text[len(text) - index -1]
    
    return revers_text

print(reversing_chains("Hola mundo"))