import random
capitalcity = {'korea':'seoul', 'USA':'washington dc', 'france':'paris', 'china':'beijing', 'japan':'tokyo'}
thelist = []
thelist1 = []
for key, value in capitalcity.items():
    thelist.append(key)
    thelist1.append(value)

a = random.choice(thelist)
while True:
      print('what is the capital of ', a)
      b = input('input:')
      b = b.lower()
      print(b)
      if capitalcity[a] == b:
          print("correct!!!!")
          break
      else:
          print("try again!!!")
          continue
