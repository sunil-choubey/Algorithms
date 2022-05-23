import string
def printbinary(list1,n):
    if n <0:
        print(list1)
        return
    list1[n-1] = 0
    print("Before", list1,n)
    printbinary(list1,n-1)
    list1[n-1] =1 
    print("After" , list1,n)
    printbinary(list1,n-1)

n=2
listA=[None]*2
printbinary(listA,n)

print(list(map(int,string.digits)))

    