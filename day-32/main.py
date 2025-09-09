s1 = {1,2,3}
s2 = {3, 5,6}
print(s1.union(s2))
print(s1.intersection(s2))
cities = { 'Chicago'}
# cities = {'New York', 'Los Angeles', 'Chicago'}
# cities1 = {'Chicago'}
cities1 = {'Chicago', 'Houston', 'Phoenix'}
# print(cities.isdisjoint(cities1))
# print(cities.difference(cities1))
# print(cities.symmetric_difference(cities1))
print(cities.issuperset(cities1))
print(cities.issubset(cities1))