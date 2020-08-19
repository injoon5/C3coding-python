import copy

c1 = ['New York', 'Tokyo']
c2 = ['Paris', 'London']
c3 = ['New York', 'Tokyo']

c1.insert(1, 'LA')
print(c1)
c1.insert(2, 'Seoul')
print(c1, end='\n\n')

c1.extend(c2)
c3.append(c2)
print(c1)
print(c3, end='\n\n')

shallow_cpy = c3[:]
shallow_cpy.insert(1, 3)
c3.insert(1, 4)
print(shallow_cpy, c3, end='\n\n')

deep_cpy = copy.deepcopy(c3)
shallow_cpy[3].append(7)
deep_cpy[3].append(8)
c3[3].append(9)
print(c3)
print(shallow_cpy)
print(deep_cpy)
