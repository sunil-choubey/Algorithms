#### An improved version of insertion sort
####It just tries to do a swap of records with a gap.
##### At gap =1 , It is similar to insertion sort

#### Lets say we are starting with  gap of n//2

from bubble_sort import printtimetaken
@printtimetaken
def shell_sort(list1):
    ll= len(list1)
    numofins=0
    numofcom=0
    if ll in  (0,1):
        return numofcom,numofins
    
    gap=ll//2
    while ( gap >0):
        for i in range(gap,ll):
            key = list1[i]
            inspos=i
            numofins+=1
            while (  inspos >=gap and list1[inspos-gap] > key):
                numofcom+=1
                list1[inspos] = list1[inspos-gap]
                inspos = inspos - gap
            list1[inspos] = key
            ####print(list1,gap) -- Uncomment this to see how the shell sort is working
        gap = gap//2

    
    return numofcom, numofins


if __name__ == "__main__":
    listA=[7,6,5,4,3,2,1,8]
    listB=[1,2,3,4,5,6,7]
    listC=[56,34,21,22,34,56]

    shell_sort(listA)
    shell_sort(listB)
    shell_sort(listC)