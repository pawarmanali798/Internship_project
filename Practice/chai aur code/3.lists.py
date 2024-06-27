myList=["don","snow","leo","bittu"]
myList[2]="tiger"
print(myList) #['don', 'snow', 'tiger', 'bittu']
myList[1:2]="monty"
print(myList)  #['don', 'm', 'o', 'n', 't', 'y', 'tiger', 'bittu']
myList[1:2]=["monty"]
print(myList)#['don', 'monty', 'o', 'n', 't', 'y', 'tiger', 'bittu']
