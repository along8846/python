def foo(x,y,z,*args,**kargs):
    print(x)
    print(y)
    print(z)
    print(args)
    print(kargs)

foo('along',3,'python')
foo(1,2,3,4,5)
foo(1,2,3,4,5,name='along')
