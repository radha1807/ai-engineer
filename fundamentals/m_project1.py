# device hierarchy (same from poly.py file)

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
    

class	TestResult:
    def	__init__(self,	test_name,	device,	passed,	error_msg=None):
        self.test_name	=	test_name
        self.device	=	device		#	composition	—	the	WHOLE	device	object
        self.passed	=	passed
        self.error_msg	=	error_msg
        
    def	line(self):
        status	=	"PASS"	if	self.passed	else	f"FAIL	({self.error_msg})"
        return	f"[{self.device.name}]	{self.test_name}:	{status}"
    
 #	----	Build	the	devices	(polymorphism-ready:	different	types,	same	list	later)	----   

y = spidevice('amd',100 , 3)
q = memory('flash memory',345 , 2,500)
z = module('intel',150, 3,250)



results	=	[
    TestResult("Mode	Check",	y,	True),
    TestResult("Clock	Sync",	q,	False,	"timeout	after	200ms"),
    TestResult("Data	Integrity",	y,	True),
    TestResult("Power	Rail	Check",	q,	True),
    TestResult("Focus	Calibration",	z,	False,	"out	of	range"),
]



#	----	Print	device	inventory	first	(polymorphism	—	one	loop,	mixed	types)	----
print("===	Device	Inventory	===")
for	device	in	[y,	q,	z]:
    print(device.summary())
    
    
#	----	Compute	and	print	the	overall	pass	rate	----
passed_count	=	sum(1	for	r	in	results	if	r.passed)
total_count	=	len(results)
pass_rate	=	(passed_count	/	total_count)	*	100
print(f"\n===	Summary	===")
print(f"Pass	rate:	{passed_count}/{total_count}	({pass_rate:.1f}%)")


#	----	Print	just	the	failures,	with	full	device	context	----
failed_results	=	[r	for	r	in	results	if	not	r.passed]
print(f"\n===	Failures	({len(failed_results)})	===")

for	r	in	failed_results:
    print(f"		-	{r.device.name}:	{r.test_name}	--	{r.error_msg}")
























print(y.summary())
print(q.summary())
print(z.summary())

# adding test results


q = memory('flash memory',345 , 2,500)
result	=	TestResult("Clock	Sync",	q,	False,	"timeout	after	200ms")

print(result.line())