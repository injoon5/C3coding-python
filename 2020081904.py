t1 = ('one', 2, 3.0)
t2 = (4, 5)
t3 = ('one', 2, 3.0)
t4 = t3 + t2

for item in t4:
      print(item, end=", ")
print()

if 'one' in t3:
      print("There is 'one' in the t3.", end='\n\n')

unpk1, unpk2, unpk3 = t1
print(unpk1, unpk2, unpk3)
print('The t1 tuple is {0}.'.format(t1), end='\n\n')

t5 = ('nested', t1, t2)
print(t5)
print(t5[1][1])
