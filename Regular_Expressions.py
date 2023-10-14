### Regular Expressions ###

import re
import string

# match

my_string = "Esta es la lección número 7: Lección llamada Expresiones Regulares"
my_other_string = "Esta no es la lección número 6: Manejo de ficheros"

match = re.match("Esta es la lección", my_string,re.I)
print(match)
print(match.span())
start, end = match.span()
print(my_string[start:end])
print(match.group())



match = re.match("Esta no es la lección", my_other_string)
# if not(match == None): # Otra forma de comprobar el None
# if match != None: # Otra forma de comprobar el None
if match is not None:
    print(match)
    start, end = match.span()
    print(my_other_string[start:end])

print(re.match("Expresiones Regulares", my_string))

# # search

search = re.search("lección", my_string, re.I)
print(search)
start, end = search.span()
print(my_string[start:end])
print(search.group())

# findall

findall = re.findall("Esta es", my_string)
print(findall)

#split

print(re.split(" ", my_string))

# sub

print(re.sub("[l|L]ección", "LECCIÓN", my_string))
print(re.sub("Expresiones Regulares", "RegEx", my_string))

# Clase en vídeo (09/11/22): https://www.twitch.tv/videos/1648023317

### Regular Expressions Patterns ###

# Para aprender y validar expresiones regulares: https://regex101.com

pattern = r"[lL]ección"
print(re.findall(pattern, my_string))

pattern = r"[lL]ección|Expresiones"
print(re.findall(pattern, my_string))

pattern = r"[0-9]"
print(re.findall(pattern, my_string))
print(re.search(pattern, my_string))

pattern = r"\d"
print(re.findall(pattern, my_string))

pattern = r"\D"
print(re.findall(pattern, my_string))

pattern = r"[l].*"
print(re.findall(pattern, my_string))


email = "mouredev@mouredev.es"
pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z-.]"
print(re.match(pattern, email))
print(re.search(pattern, email))
print(re.findall(pattern, email))

email = "mouredev@mouredev.com.mx"
print(re.findall(pattern, email))



### What is the most frequent word in the following paragraph? ###

def most_frequent_word(paragraphs:str):
    pattern = r'[ ]'
    frequent_word_list = re.sub('\.','',paragraphs)
    frequent_word_list_split = re.split(pattern,frequent_word_list)
    str(frequent_word_list)
    words_list = list()
   
    for word in frequent_word_list_split: 
         words_list.append( (len(re.findall(word,frequent_word_list))  , word))
   
    words_list_delete_duplicate = list()
    for dupla in words_list:
        if dupla not in words_list_delete_duplicate:
            words_list_delete_duplicate.append(dupla)
    
    words_list_delete_duplicate.sort()
    words_list_delete_duplicate.reverse()


    for dupla in words_list_delete_duplicate: 
          print(dupla)


paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'
most_frequent_word(paragraph)



# this square bracket means either A or a
regex_pattern = r'[Aa]pple|[Bb]anana|[Dd]octor' 
txt = 'Apple and banana are fruits. An old cliche Doctor says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away.'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['Apple', 'banana', 'apple', 'banana']



# search a ward with :
mi_string = "Tu madre tiene una hermano: que a su ves tiene un padre"
patron = r"[a-z]"
respuesta = re.findall(patron,mi_string)
print(respuesta)




def find_distance(text:str)->str:
    anum = []
    for num in text:
      if re.search('(a-z)',num) == None:          
          anum.append(int(num))
      else: return "Error de entrada"
      
    
    return f"{anum[-1]} -({anum[0]})"

points = ['-12', '-4', '-3', '-1', '0', '4', '8']
print(find_distance(points))




## Write a pattern which identifies if a string is a valid python variable

def is_a_valid_python_variable(valid_variable):
    try:
     re.search(r"(^[a-zA-Z_])(\w*$)",valid_variable).group()
     return True

    except: return False
 
word = "_firs4tname"
print(is_a_valid_python_variable(word))




