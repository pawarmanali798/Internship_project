# x=10

# def func():
#     global x
#     x=20
#     print(x)

# print(x)
# func()

def func1():
    x=10
    def func2():
        print(x)
    return func2

myResult=func1()
myResult()