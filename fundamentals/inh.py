class students:
    def __init__(self, name, age,gender):
        self.name = name 
        self.age = age
        self.gender = gender
        
    def summary(self):
        return f"{self.name} , {self.age}, {self.gender}"
    
    
class activities(students):
    def __init__(self,name, age , gender, type):
        super().__init__(name,age,gender)
        self.type = type
        
a = activities('gita,', 22, 'F,' , 'badminton')

#print('the name,age and gender of the student is ::', a.name, a.age , a.gender)

print('name : ', a.name)
print('age : ',a.age)
print('gender : ', a.gender)
print('activity doing : ', a.type)


#EXAMPLE 2

class school:
    def __init__(self,name,city,board):
        self.name = name 
        self.city = city 
        self.board = board 
    
class sports(school):
    def __init__(self,name,city,board,sport):
        super().__init__(name,city,board)
        self.sport = sport
        
x = sports('SMVM  |', 'chandrapur   |', 'cbse   |', 'cricket')
y = sports('BJM   |' , 'chandrapur  |' , 'state |', 'tennis')

print('school 1: ', x.name, x.city , x.board, x.sport)   
print('school 2: ', y.name, y.city, y.board, y.sport)   


#EXAMPLE 3 


class bank:
    def __init__(self,name,type,city):
        self.name = name 
        self.type = type 
        self.city = city
        
    def summary(self):
        return f"{self.name} {self.type} {self.city}"
        
class customers(bank):
    def __init__(self,name,type,city,c_name):
        super().__init__(name,type,city)
        self.c_name = c_name 
        
    def summary(self):
        return f"{super().summary()} {self.c_name}"
        
x = customers('sbi    |' , 'govt |' , 'nagpur |','radha')
y = customers('hdfc   |' , 'pvt  |' , 'delhi  |','radhika ')
z = customers('canara |' , 'govt |' , 'raipur |','anmol')


print(x.summary(), x.c_name) 
print(y.summary(), y.c_name)
print(z.summary(), z.c_name)
print('=====================================')
print(x.summary())
print(y.summary())
print(z.summary())
print('=====================================')
print('name of the bank: ', x.name , 'govt/pvt: ', x.type, 'city: ', x.city , 'customer name: ', x.c_name )

print('name of the bank: ', y.name , 'govt/pvt: ', y.type, 'city: ', y.city , 'customer name: ', y.c_name )

print('name of the bank: ', z.name , 'govt/pvt: ', z.type, 'city: ',z.city , 'customer name: ', z.c_name )


#EXAMPLE 4 OVERRIDING

class state:
    def __init__(self, name,cities):
        self.name = name 
        self.cities = cities 
        
class city(state):
    def __init__(self,name,cities,place):
        super().__init__(name,cities)
        self.place = place
        
x = city('kerala', 'munnar',"tea garden")
y = state('gujarat', 'somnath')

print(x.name, x.cities, x.place)

