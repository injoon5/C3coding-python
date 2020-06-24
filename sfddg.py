def myplus(n1st, n2st):
      return n1st+n2st

def myminus(n1st, n2st):
      return n1st-n2st

def mymul(n1st, n2st):
      return n1st*n2st

def mydiv(n1st, n2st):
      return n1st/n2st

n1stnum = int(input('숫자1'))
n2stnum = int(input('숫자2'))
choose = input('연산자')

if choose == "+":
      nstr1 = myplus(n1stnum, n2stnum)
      print(nstr1)

if choose == "-":
      nstr1 = myminus(n1stnum, n2stnum)
      print(nstr1)

if choose == "*":
      nstr1 = mymul(n1stnum, n2stnum)
      print(nstr1)
