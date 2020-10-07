class Car:
      color = ''
      speed = 0

      def upSpeed(self, value):
            self.speed = value

Car1  = Car()
Car2  = Car()
Car3 = Car()

Car1.color = '검정'
Car2.color = '빨강'
Car3.color = '파랑'

Car1.upSpeed(70)
Car2.upSpeed(90)
Car3.upSpeed(50)


print('자동차 1의 색깔은', Car1.color, '이고, 속도는 ', Car1.speed, 'km 이다.')
print('자동차 2의 색깔은', Car2.color, '이고, 속도는 ', Car2.speed, 'km 이다.')
print('자동차 3의 색깔은', Car3.color, '이고, 속도는 ', Car3.speed, 'km 이다.')
