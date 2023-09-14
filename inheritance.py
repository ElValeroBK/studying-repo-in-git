class animal():
    def walk(self):
        print("walk")

class hog(animal):  #inheritanc (herencia) 
    def vocalize(self):
        print("vocalize")
    pass  # (pass) mean the class it ok would be a emty class

class cat(animal):
    def meows(self):
        print("meows")

pitchi = cat()
pitchi.meows

picho = hog()
picho.walk
