class Car:
      speed = 'low'
      gear = '2'
      color = 'blue'

      def speedChange(self, v):
            print('sppedChange-->')
            self.speed = v

      def gearChange(self, v):
            print('gearChange-->')
            self.gear = v

ccubeCar = Car()

print(ccubeCar.speed)
print(ccubeCar.gear)
print(ccubeCar.color)

ccubeCar.speedChange('high')
print(ccubeCar.speed)
ccubeCar.gearChange('4')
print(ccubeCar.gear)

