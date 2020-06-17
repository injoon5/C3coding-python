import random as r

fruitlist = ['apple', 'banana', 'orange']

myfruit = r.choice(fruitlist)

myfruitlist = list(myfruit)

r.shuffle(myfruitlist)

whatfruit = ' '.join(myfruitlist)

print("힌트:", whatfruit)


while True:
    a = input("answer:")
    
    if a != myfruit:
        print('try again')
        continue
        
    else:
        break
        
print("you won!")

        
