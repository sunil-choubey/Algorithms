#### Sort algorthim which tries to Find the minimum element in the list and replace it with the first element
#### 5,4,3,2,1
#### Next iteration will become 1,4,3,2,5
####next Iteration will be 1,2,3,4,5
#### But selection sort will run 5*4*3*2*1 times.

from numpy import minimum
from bubble_sort import printtimetaken

@printtimetaken
def selection_sort(list1:list[int]) -> int:
    ll = len(list1)
    if ll == 0:
        return 0,0
    temp=list1[0]
    numberofiter=0
    numberofcom=0
    minpos=0
    for i in range(ll):
        minpos=i
        for j in range(i+1,ll):
            numberofiter +=1
            if list1[j] < list1[minpos]:
                numberofcom +=1
                minpos=j
        ### We have found the minimum value position in the list , now swap the sme with its element data
        temp = list1[minpos]
        list1[minpos] = list1[i]
        list1[i] = temp
    else:
        print(list1)
        return numberofcom,numberofiter

if __name__ == "__main__":
    listA = [7,6,5,4,3,2,1]
    listB = [1,2,3,4,5,6,7]
    selection_sort(listA)
    selection_sort(listB)
