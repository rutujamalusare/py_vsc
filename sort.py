def sortByLength(e):
    return len(e)


cities= ["ab","vffff","riifiiishi","thudfhuhf","vkk","s"]
print(cities)
cities.sort
print(cities)
cities.sort(reverse=True)
print(cities)

cities.sort(key=sortByLength)
print(cities)

