cities = ['Seoul', 'New York', 'London', 'Tokyo', 'LA']
gdp = [779.3, 1210, 731.2,1520, 789.7]
mix = ['A', 'B', 'B', 1, 1, 2, 3]

cities.sort()
print(cities)
cities.sort(reverse=True)
print(cities)
gdp.sort()
print(gdp)
gdp.sort(reverse=True)
print(gdp, end="\n\n")

#mix.sort()
mix.reverse()
print(mix, mix.count('B'), mix.count(1))

print(cities.pop(), cities)
print(cities.pop(), cities)

mix.remove(1)
cities.remove('Tokyo')
print(mix, cities)
print(cities.index('Seoul'), cities.index('New York'))
