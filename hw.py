import random asrandom as r

      fruitlist = ['apple', 'banana', 'orange', 'mango', 'strawberry', 'hanlabong', 'grape', 'blueberry', ]

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
        
      print("you won!",'to try again, press 1.')
      startagain = input('press 1 to restart, press anything else to end.')
      if startagain == "1":
                       
                       continue
      else:
                       break
      
      

        
