import random
num=int(input("enter a number:"))

mylist=[]
for i in range(100):
    mylist.append(random.randint(1,1000))
for nums in mylist:
    if (nums==num):
        print("you found it")
        break
    else:
        print(str(num) + " is not in the list")
        break
            
mylist.sort()
print("the list is:" + str(mylist))
    