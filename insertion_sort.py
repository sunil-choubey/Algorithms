###### Insertion Sort works like :
###### 1) Start with Position i in the array considering all the element before i are sorted. 
###### 2) If the value at i is < value i -1 then switch values at i -1 to right of i 
###### 3) Insertion sort will start from 1 

from bubble_sort import printtimetaken
@printtimetaken
def insertion_sort(list1:list[int]) -> int:
    ll = len(list1)
    if ll ==0:
        return 0,0
    temp = list1[0]
    inspos=0
    numofiter=0
    numofcom=0
    for i in range(1,ll):
        key=list1[i]
        j = i
        numofiter=0
        while (j >= 0):
            numofcom=0
            if list1[j-1] > list1[j]:
                list1[j]= list1[j-1]
            
        list1[j] = key
    
    return numofcom,numofiter

if __name__ == "__main__":
    listA=[7,6,5,4,3,2,1]
    listB=[1,2,3,4,5,6,7]
    listC=[56,34,21,22,34,56]

    insertion_sort(listA)
    insertion_sort(listB)
    insertion_sort(listC)
