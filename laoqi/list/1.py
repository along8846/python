alst = [1, 2, 3, 4, 5, 6]
print(alst[::-1])
print(alst[-1::-1])
print(alst[-1:-len(alst)-1:-1])
print(alst[-1:-7:-1])
print(alst[-1:-6:-1])

"""
[6, 5, 4, 3, 2, 1]
[6, 5, 4, 3, 2, 1]
[6, 5, 4, 3, 2, 1]
[6, 5, 4, 3, 2, 1]
[6, 5, 4, 3, 2]
"""
    


print(list(reversed(alst)))