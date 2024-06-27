#find positive number

# listNumber=[2,-3,-6,-5,3,4,6,8,10.11,-34,-88]

# postiveList=[]
# for x in listNumber:
#     if x >=0:
#         postiveList.append(x)
# print(postiveList)

#even numbers sum

# rangeNumber=int(input("Enter the number:"))

# sumNumber=0
# for x in range(rangeNumber + 1):
#     if x % 2==0:
#         sumNumber+=x

# print(sumNumber)

#multiplication of number skip the 5th iteration

# number=int(input("Enter the number:"))

# for x in range(1,11):
#     if(x==5):
#         continue
#     mul=number*x
#     print(mul)

#reverse the string 

# originalStr="Python"
# reverseStr=""
# for char in originalStr:
#     reverseStr= char+ reverseStr
# print(reverseStr)


#find first non repeating character in list
# inputList=['a','b','a','d','b','z','a','a','s','s']
# uniqueList=[]
# for x in inputList:
#     if x not in uniqueList:
#         uniqueList.append(x)
# print(uniqueList)
# character=uniqueList[0]
# print("So the first non repeating character is "+character)

# #find first non repeating character in string
# #1st approch
# inputString="teeter"
# uniqueString=""
# for char in inputString:
#     if char not in uniqueString:
#         uniqueString +=char
#         # break
# print(uniqueString)
# nonRepeatingChar=uniqueString[0]
# print("So the first non repeating characters are "+nonRepeatingChar)

#2nd approch
# newString="teeter"
# for char in newString:
#     newString.count(char)==1
#     print(char)
#     break

#fact

# num=int(input("Enter number:"))
# factorial=1
# for x in range(1,num+1):
#     factorial=factorial*x
# print(factorial)


# while True:
#     userInput=int(input("Enter the number:"))
#     if 1<=userInput<=10:
#         print("Thanks")
#         break
#     else:
#         print("Invalid")

#primenumber

number=int(input("Enter number:"))

while number > 1:
    for x in range(2,number):
        if number % x==0:
            is_prime=False
            break
        else:
            is_prime=True
    break   
print(is_prime)



