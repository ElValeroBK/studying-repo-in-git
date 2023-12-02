# exructure of the class
'''class Car:  
#constructors
    def __init__(self,fors,cherolet):
        self.fors = fors
        self.cherlot = cherolet                     
    def run(self):
        print("run")
    
    def stop(self):
        print("stop")
    

car1 = Car(4,7)
print(car1.fors)
car1.x=8
print(car1.x)
car1.run()
car1.x = "llo"
print(car1.x)

car2 = Car(5,9)
car2.y=10
print(car2.y)
car2.stop() '''

# task
'''class Person:
    #constructors
    def __init__(self,name):
        self.name=name
    #funtion
    def talk(self):
        print("talk")

#object
juan = Person("karla")
print(juan.name)
juan.talk()'''


class Contruction():
    def __init__(self,room,sala):
        self.room= room
        self.sala=sala  
        self.__room = room + sala  # propiedad pribada (__room)
    def rooms(self):
        return self.__room      
    def home(self):
        print(f'I am a beautiful House with {self.room} room')
    def hotel(self):
        print(f'I am a beautiful Hotel')
        


newyork=Contruction(5,1)      #Object (newyork)
print(newyork.room)
print(newyork.sala)
#print(newyork.__room)
print(newyork.rooms())












    