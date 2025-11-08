
#CONSTRUCTOR   USES:-

class Animal:
    def __init__(self, species):
        self.species=species
        
# def sound(self):
#     print("All animals make sound")
    
    
class Dog(Animal):
    def __init__(self, species, breed):
        super().__init__(species)
        self.breed=breed
        print(species, breed)
        
dog1=Dog("Mammal", "Labrador")        
                   
                   
                   
                   
#METHOD USES:-                   



class Animal:
    def __init__(self, species):
        self.species=species
        
def sound(self):
    print("All animals make sound")
    
    
class Dog(Animal):
    def __init__(self, species, breed):
        super().__init__(species)
        self.breed=breed
        print(species, breed)
        
        
    def sound(self):
        super().sound()
        print("Barks!!!!!")
            
        
dog1=Dog("Mammal", "Labrador")  
dog1=sound()      
                   