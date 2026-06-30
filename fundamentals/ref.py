class planets:
    def __init__(self,name,moons):
        self.name = name 
        self.moons = moons 
        
class objects:
    def __init__(self, type,sides):
        self.type = type
        self.sides = sides 
        
        
source_a = planets("earth",1)
source = objects("square",source_a)

print(" planet", source.sides.moons)

    