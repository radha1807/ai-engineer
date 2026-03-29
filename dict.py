messages = [{"role":"user","content":"Hello"}, {"role":"assistant","content":"Hi!"}] 
texts = [m["content"] for m in messages] 
print(texts)

words = ['cast', 'elephant','ox']
lengths = [len(w) for w in words]
print(lengths)

results = [x*2 for x in [2,6,92,81]]
print(results)

fruits = ['cherry','berries', 'mango','pineapple']
value = [len(f) for f in [fruits]]
print(value)


person = {"name": 'arpita', 'age': '23', 'sub':'bio'}

print(person['name'])
print(person['age'])
person['salary'] = '50,000' #the value is added to dict
print(person)
del person['sub']
print(person)