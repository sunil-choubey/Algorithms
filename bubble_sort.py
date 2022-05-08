### We need to sort the highest number in the end
### Example Given a sequence 4,3,2,1
### In the first iteration the result should be 3,2,1,4
## It just compares a[j-1] with a[j] and if a[j] > a[j-1] 

from datetime import datetime
from time import sleep

def printtimetaken(func):

    def innerfunc(*args,**kwargs):
        starttime = datetime.now()
        sleep(5)
        numofconditions,numofiterations = func(*args,**kwargs)

        endtime = datetime.now()
        print(f"Time taken to execute {func.__name__} is {endtime - starttime} and total iterations done = {numofiterations} and total conditions evaluated- {numofconditions}")
    return innerfunc


@printtimetaken   ## use Of Decorators in python
def bubble_sort(list1: list[int]) -> int:
    lenL= len(list1)
    numofiter=0
    numofcond=0
    if lenL == 0:
        print(f"The List is empty")
        return 0,0
    
    for _ in range(lenL):
        for j in range(lenL-1):
            numofiter+=1
            if list1[j + 1] < list1[j]:
                numofcond+=1
                temp=list1[j]
                list1[j] = list1[j+1]
                list1[j+1] = temp
    else:
        print(list1)
    return numofiter,numofcond

@printtimetaken
def bubble_sort_swap(list2:list[int]) -> int:
    ll = len(list2)
    numofiter=0
    numofcond=0
    if ll == 0:
        print("The list is empty")
        return 0,0
    temp=list2[0]
    for _ in range(ll):
        swap=False                  #### Setting up a swap variable which will take care of a sorted list
        for j in range(ll-1):
            numofiter +=1
            if list2[j]> list2[j+1]:
                numofcond +=1
                temp=list2[j]
                list2[j] = list2[j+1]
                list2[j+1] = temp
                swap = True
        if not swap:
            print(list2)
            return numofcond,numofiter
    else:
        print(list2)

if __name__ == "__main__":
    listA = [7,6,5,4,3,2,1]
    listB = [1,2,3,4,5,6,7]
    bubble_sort(listA)
    bubble_sort(listB)
       
    listA = [7,6,5,4,3,2,1]
    listB = [1,2,3,4,5,6,7]
    ### Calling new Bubble_sort_swap
    bubble_sort_swap(listA)
    bubble_sort_swap(listB)