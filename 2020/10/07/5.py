class Car:
      name = ''
      color = ''
      speed = 0

      def __init__(self, value1, value2, value3):
            self.color = value1
            self.speed = value2
            self.name = value3
      
      def upSpeed(self, value):
            self.speed = value

Car1  = Car('검정', 70, '람보르기니')
Car2  = Car('빨강', 90, '딜로리안(망...)')
Car3 = Car('파랑', 50, '포터르기니')

 


print('%s의 색깔은 %s 색이고, 속도는 %d km 이다.'% (Car1.name,Car1.color,Car1.speed))
print('%s의 색깔은 %s 색이고, 속도는 %d km 이다.'% (Car2.name,Car2.color,Car2.speed))
print('%s의 색깔은 %s 색이고, 속도는 %d km 이다.'% (Car3.name,Car3.color,Car3.speed))

