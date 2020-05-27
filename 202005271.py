for num in range(1, 10+1):
    if(num % 3) == 0:
        continue
    print(num, end='+1 = ')
print()

for num in range(20,50+1):
    if(num %2) == 0 and (num %3)==0:
        print(num, end=". what?!?!")
        break
