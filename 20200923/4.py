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
