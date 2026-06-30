#setting instance attribute 
#method_1

''''class spidevice:
    def __init__(self,name,clk_speed):
        self.name = name
        self.clk_speed = clk_speed
        
    def rename(self,new_name):
        self.name = new_name
        
obj_1 = spidevice('imu-sensor', 20)
obj_2 = spidevice('flash memory', 40)

obj_1.rename('imu_sensor12')

print('obj_1',obj_1.name)
print('obj_2', obj_2.name)'''

#method_1
class spidevice:
    def __init__(self,name,distance):
        self.name = name
        self.distance = distance
        
chart1 = spidevice('A-class',200)
chart2 = spidevice('B-class',240)

print('method 1 results')
print('the total dist covered by', chart1.name , chart1.distance )
print('the total dist covered by',chart2.name, chart2.distance)

if (chart1.distance > chart2.distance):
    print('winner is : ', chart1.name, chart1.distance)
else:
    print('the winner is: ',chart2.name, chart2.distance)
    

#method 2  Set	directly	from	outside,	after	the	object	already	exists

class	SPIDevice:
    def	__init__(self,	name):
        self.name	=	name
sensor	=	SPIDevice("IMU-Sensor")
#adding	a NEW attribute	directly from outside the class, after creation
sensor.clock_speed_mhz	=	10

print("Set directly from outside:(method_2)",	sensor.name, sensor.clock_speed_mhz)


#method 3 set method

class spidevice:
    def __init__(self, name,env):
        self.name = name
        self.env = env
        
sensor = spidevice('imu-chip', 'stable')

print('the sensor reading is(method-3): ', sensor.name, sensor.env)
    



