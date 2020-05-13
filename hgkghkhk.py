import random

a = random.randint(1,100)
b = 5


while b>-1:

    c = int(input("num1"))
    
    if a == c:
        print('you won!')
        
    if c>a:
        print('down. ',b,"left")
      
        b = b-1
        
    if c<a:
        print('up. ',b,"left")
        
        b = b-1
        
    if b<0:
        print('you lost','the answer was',a,';·)')
    

    
              
