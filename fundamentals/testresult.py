class testresults:
    def __init__(self, name,passed):
        self.name = name
        self.passed = passed
        
test_result_1 = testresults('spi mode check', True)
test_result_2 = testresults('clock sync', False)

print('the result 1 is: ' , test_result_1.name , 'passed:', test_result_1.passed)
print('the result 2 is: ', test_result_2.name, 'paased: ',test_result_2.passed)

