###### Insertion Sort works like :
###### 1) Start with Position i in the array considering all the element before i are sorted. 
###### 2) If the value at i is < value i -1 then switch values at i -1 to right of i 
###### 3) Insertion sort will start from 1 

from bubble_sort import printtimetaken
@printtimetaken
def insertion_sort(list1:list[int]) -> int:
    ll = len(list1)
    numofiter=0
    numofcom=0
    if ll==0:
        return numofcom,numofiter
    ### Start with second  element of the list considering first is sorted and now check if second element is less than first element
    ### if yes then move keep second element in a temp column and move the first column to the position 
    ### now position of first element is blank so put the temp value in the first element , this is why it is called insertion sort
    for i in range( 1 , ll):
        key = list1[i]  
        inspos=i      
        for _ in range(i,0,-1):
            numofiter +=1
            if list1[inspos-1] > key:
                numofcom +=1
                list1[inspos] = list1[inspos-1]
                inspos-=1
            ### Position of inspos is decremented by 1 
        else:
            pass
        list1[inspos] = key
    else:
        print(list1)
    return numofcom,numofiter
    


if __name__ == "__main__":
    listA=[7,6,5,4,3,2,1]
    listB=[1,2,3,4,5,6,7]
    listC=[56,34,21,22,34,56]

    insertion_sort(listA)
    insertion_sort(listB)
    insertion_sort(listC)
