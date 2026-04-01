def add(a , b):
    return a+b

print(add(2,3))



def name(x,y):
    return x &y
print(name(4,2))



def num_all(*args):
    return sum(args)
print(num_all(1,2,4,9,6))



def  config(**kwargs):
    for key, value in kwargs.items():
        print(key, "=", value)
config(model="gpt-4o", temperature=0.7, max_tokens=500)


def config(**kwargs):
    for key , value in kwargs.items():
        print(key, '=', value)
config(model= 'gpt4',temp = 0.4, max_tokens = 400)




def full_example(required, *args, keyword_only='default', **kwargs):
    print(f'required: {required}')
    print(f'extra positional args: {args}')
    print(f'keyword_only: {keyword_only}')
    print(f'extra keyword args: {kwargs}')
    
full_example('hello', 1, 2, 3, keyword_only='custom', debug=True, version=2)


def order_pizza(size, *toppings, crust='thin', **extras):
    print(f'Size: {size} | Toppings: {toppings} | Crust: {crust} | Extras: {extras}')

#method1
def double(x):
    return x * 2
print (double(2))

#method2
double_lambda = lambda x:x*2
double(5)
print(double_lambda(5))