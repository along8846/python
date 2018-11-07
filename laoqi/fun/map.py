items = [1,2,3,4,5]


print(map(lambda x : x**2, items))


print([x**2 for x in items])


lst1 = [1, 2, 3, 4, 5]
lst2 = [6, 7, 8, 9, 0]
map(lambda x, y: x + y, lst1, lst2)
print([x+y for x,y in zip(lst1,lst2)])
print([ max(x,y) for x,y in zip(lst1,lst2)])


lst1 = [1, 2, 3, 4, 5]
lst2 = [6, 7, 8, 9, 0]
lst3 = [7, 8, 9, 2, 1]
map(lambda x,y,z: x+y+z, lst1, lst2, lst3)
