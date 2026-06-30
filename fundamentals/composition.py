class tree:
    def __init__(self,name,height):
        self.name = name
        self.height = height
    
class chocolate:
    def __init__(self,company,tree):
        self.company = company
        self.tree= tree
        
    def summary(self):
        tree_info = f"{self.tree.name}tree | {self.tree.height}m tall "
        return f"[{tree_info}] company: {self.company}"
        
oak = tree("Oak-No-7", 12)

# ---- Create a Chocolate that stores the WHOLE oak object ----
choco = chocolate("kitkat", oak)

# now we CAN reach height_m and fruit_count, because we kept the real object
print("Tree height in meters:", choco.tree.height)
print(choco.summary())





# example 2 

class laptop:
    def __init__(self, brand, ram_gb):
        self.brand = brand 
        self.ram_gb = ram_gb

class backpack:
    def __init__(self,color,laptop):
        self.color = color
        self.laptop = laptop
        
    def summary(self):
        laptop_info = f"{self.laptop.brand} | {self.laptop.ram_gb} GB RAM"
        return f"[{laptop_info}] backpack color: {self.color} " 
    

dell = laptop('dell',256)
bag = backpack('black',dell)

print('ram : ', bag.laptop.ram_gb)
print(bag.summary())    


#example 3

class student:
    def __init__ (self, name,gender,age):
        self.name = name
        self.gender = gender 
        self.age = age 
        
class school:
    def __init__(self,name,city):
        self.name = name 
        self.city = city 
        self.student = student 
        
    def summary(self):
        student_info = f"[{self.student.name} || {self.student.gender} || {self.student.age}]"
        return f"[{student_info}]"
    
S1 = student('ram','male',22)
S2 = student('anu','female',21)

school1 = school('smvm','chandrapur',S1)
school2 = school('xaviers','delhi',S2)

print('gender', school1.student.gender)
print(school1.summary())
        