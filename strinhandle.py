linus = "Talk is cheap. Show me the code. - Linus Torvals"
alphanum = "C3coding"
num = "12345"
up_case = linus[:4].upper()
lo_case = linus[:4].lower()

print(up_case.isupper(), up_case.islower())
print(lo_case.isupper(), lo_case.islower(), end="\n\n")

print(linus.isalpha(), up_case.isalpha())
print('-'.isalpha(), ' '.isalpha(), '.'.isalpha(), end="\n\n")

print(alphanum.isalnum(), num.isalnum(), up_case.isalnum())
print(linus.isalnum(), 'Steve jobs.'.isalnum(), end="\n\n")

print(num.isdecimal(), alphanum.isdecimal, linus.isdecimal())
print(linus.isspace, ' '.isspace(), end="\n\n")

print("Do Your Best".istitle(), linus.istitle())
