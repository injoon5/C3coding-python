height =int(input("your height : "))

if height<110:
    print("Do not enter!")
if height>= 110:
    print("have a nice time!")
if height == 110:
    print("perfect!")
if height != 110:
    print("Not 110.")
if 100 <= height <110:
    print("Next year~")
print("Booltype = ", height< 110,height >= 110, height == 110)
print("Booltype =", height != 110, 100 <= height < 110)
