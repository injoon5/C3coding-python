while True:
    a = input("input plz: ")
    b = ''.join(reversed(a))

    if a == b:
        print("the word is a palindrome!!")
    else:
        print("that isnt a palindrome!!!")
    ifstart = input("do you want to restart? if yes press 1, if not press any other key.")
    if ifstart == "1":
        continue
    else:
        break
