t1 = ('one', 2, 3.0)
t2 = tuple(['one', 2, 3.0])
t3 = 'one', 2, 3.0
t4 = tuple('C3coding')
t5 = tuple(range(1, 5))

print(t1, t2, t3)
print(t4, t5, end="\n\n")
#t1[0] = 'zero'
print(t1[1], t1[-1], len(t2), sep=", ")
print(t4[2], t4[2:5], len(t4), sep=", ")
print(''.join(t4), end='\n\n')

t6 = (1)
t7 = (1,)
print(t6, type(t6))
print(t7, type(t7))
