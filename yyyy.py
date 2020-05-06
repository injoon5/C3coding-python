counter1 = counter2 = 1

while counter1 < 6:
    counter2 *= counter1
    print(str(counter1)+'1 =',counter2)
    counter1 += 1

while counter1 > 0 and counter1 > counter2:
    print("NO!!!!!!!!!!")
    counter1 -= 1

blood = input("What is my blood type?")

while blood != "O":
    blood = input("Try again,What is my blood type? ")

print("Correct! Thank you")
