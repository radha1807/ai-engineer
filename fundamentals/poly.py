class spidevice:
    def __init__(self,name,clkspeed, mode):
        self.name = name 
        self.clkspeed = clkspeed 
        self.mode = mode 
        
    def summary(self):
        return f"{self.name} {self.clkspeed} {self.mode}"
    

class memory(spidevice):
    def __init__(self,name,clkspeed,mode,size):
        super().__init__(name,clkspeed,mode)
        self.size = size
        
    def summary(self):
        x = super().summary()
        return f"{x} {self.size}"
    

class module(spidevice):
    def __init__(self,name,clkspeed, mode, range):
        super().__init__(name,clkspeed,mode)
        self.range = range
        
    def summary(self):
        x = super().summary()
        return f"{x} {self.range}"
    

y = [spidevice('amd',100 , 3),
     memory('flash memory',345 , 2,500),
     module('intel',150, 3,250)]

for r in y:
    print(r.summary())
