# n = 0
# for i in range(1,6):
#     n = n + 1        
#     for j in range(0,n):
#             print("{0:>}".format("*"),end="")
#     print("")

# print("-"*20)
# for q in range(10):
#     print('{:<8}'.format(q + 1),end='')
#     print(((q+1) * '* ').center(20,' '))

print("-"*20)
for q in range(10):
    print('{:>}'.format('*' * q))
