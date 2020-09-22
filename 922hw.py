import random
capitalcity = {'korea':'seoul', 'USA':'washington dc', 'france':'paris', 'china':'beijing', 'japan':'tokyo'}
thelist = []
thelist1 = []
for key, value in capitalcity.items():
    thelist.append(key)
    thelist1.append(value)




a = random.choice(thelist)
print('what is the capital of ', a)
b = input('input:')
if capitalcity[a] == b:
    print("correct!!!!")
else:
    print("try again!!!")
