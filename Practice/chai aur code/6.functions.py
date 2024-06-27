# def even_generator(limit):
#     for i in range(2,limit + 1,2):
#         yield i

# for num in even_generator(10):
#     print(num)


#recursive factorial

def fact(num):
    if num==0:
        return 1
    else:
        return num*fact(num-1)

num=5
print(fact(5))

# def cal_Factorial(num):
#     factorial=1
#     for x in range(1,num+1):
#         factorial=factorial*x
#     return factorial
    

# num=int(input("Enter the no.:"))
# print(cal_Factorial(num))

