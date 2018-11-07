print("I like {0:10} and {1:>15}".format("python", "canglaoshi"))
# I like python     and      canglaoshi


print("I like {0:^10} and {1:^15}".format("python", "canglaoshi"))
# I like   python   and   canglaoshi

print("I like {0:.2} and {1:^10.4}".format("python", "canglaoshi"))
# I like py and    cang

print("I like {lang} and {name}".format(lang="python", name="canglaoshi"))


print("She is {0:4d} years old and the breast is {1:6.2f}cm".format(28, 90.1415926))

data = {"name":"Canglaoshi", "age":28}
print("{name} is {age}".format(**data))