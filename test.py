import this

names = ['ali', 'hasan', 'zahra', 'sara']
ages = ['17', '9', '18', '21']

for name, age in zip(names, ages):
    print(f'{name}:  {age} years old')

print(list(enumerate(names)))
# [(0, 'ali'), (1, 'hasan'), (2, 'zahra'), (3, 'sara')]


a = {'name': 'ali'}
b = {'age': 17}
a.update(b)
print(a)
# {'name': 'ali', 'age': 17}

