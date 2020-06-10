import random as r

fruitlist = ['apple', 'banana', 'orange']

myfruit = r.choice(fruitlist)

myfruitlist = list(myfruit)

random.shuffle(myfruitlist)

whatfruit = ' '.join(myfruitlist)

print("힌트:", whatfruit)
a = input("answer:")


    
    if a == whatfruit:
        print('you won!')
        
    else print("try again")
