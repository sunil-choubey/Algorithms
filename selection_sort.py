#### Sort algorthim which tries to Find the minimum element in the list and replace it with the first element
#### 5,4,3,2,1
#### Next iteration will become 1,4,3,2,5
####next Iteration will be 1,2,3,4,5
#### But selection sort will run 5*4*3*2*1 times.

from numpy import minimum


def selection_sort(list1:list[int]) -> int:
    ll = len(list1)
    if ll == 0:
        return 0,0
    
    temp =list1[0]
    
    for i in range(ll):
        minimum=list1[i]
        for j in range(i+1,ll):
            if list1[j] < minimum:
                minimum = list1[j]
            
            list1[i] = minimum


