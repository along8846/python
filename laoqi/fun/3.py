def foo(fun):
    def wrap():
        print("start")
        fun()
        print("end")
        print(fun.__name__)
    return wrap

def bar():
    print("I am in bar()")

f = foo(bar)
f()

print("*"*20)

def foo(fun):
    def wrap():
        print("start")
        fun()
        print("end")
        print(fun.__name__)
    return wrap

@foo 
def bar():
    print("I am in bar()")


bar()