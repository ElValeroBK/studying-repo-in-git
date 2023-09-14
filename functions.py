''' 
def good_neighbor(name,last_name): #definition   #parameters  #key word argument
    print(f'hello {name} {last_name}' )
    # return    return a value 


    
print("hola")
good_neighbor("john","valero")     #good_neighbor(last_name= "valero", name="john" )
'''

'''def emojis(type):     
     emoji = {
          "contencto" : "😄",
          "triste": "😒"
     }
     out=""
     words= type.split(" ")
     for emo in words :
          out+=emoji.get(emo,emo)+" "
     return out
     

print(emojis(f"hola pareces estar contencto pero a la vez triste"))'''

'''try:
     number = int(input("enter number ->  "))
     print(number)        
except ValueError:
     print("just number")
'''

try:                   #exeptions error
 
     var= input("> ")
     var1= input("> ")
     print(int(var)/var1)
except ZeroDivisionError:
     print("NO 0")
except ValueError:
     print("OJO")
except TypeError:
     print("NO STR/INT")




 