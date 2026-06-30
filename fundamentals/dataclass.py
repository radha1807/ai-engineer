'''from dataclasses import dataclass

@dataclass 
class chat:
    role: str
    content: str
    tokens: int=0
    
msg = chat('user','what is rag?',tokens = 12)
print(msg)
print(msg.role)
print(msg.tokens)'''


'''from dataclasses import dataclass

@dataclass

class config:
    role: str
    content: str
    tokens: int=0
    
msg = config('user',"what is config class?",tokens =12)
print(msg)
print(msg.role)
print(msg.tokens)'''


#using init

'''from dataclasses import dataclass

@dataclass

class env:
    role: str
    content: str
    tokens: int=0
    
msg_a = env('user','what is rag?',12)

msg_b = env(role= 'user',content = 'what is rag?', tokens=12)

msg_c = env('user','what is rag?')

print(msg_a)
print(msg_b)
print(msg_c)

print('msg_c tokens: ', msg_c.tokens)'''


#using __eq__

from dataclasses import dataclass

@dataclass

class test:
    role:str
    content: str
    tokens: int = 0
    
a = test('amy','what is your fav sub?', tokens =12)
b = test('amy', 'what is your fav sub?')
c = test('amy', 'what is your fav sub?', tokens= 12)

print('a == b', a == b)
print('a == c', a == c)

