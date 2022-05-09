######Merge Sort 
    ### recursion divide in half
    ### call merge which will just merge the two structures

def mergesort(list1,left,right):
    mid = (left + right ) //2
    ###print(list1[left:right+1],mid, left,right)
    if right > left:
        mergesort(list1,left,mid)
        mergesort(list1,mid + 1,right)
        merge(list1,left,mid+1,right)
    
def merge(list1,left,mid,right):
    print(left , mid, right, list1[left:mid], list1[mid:right+1])
    left_end = mid -1 
    size = right - left +1
    i = left
    j = right 
    new_arr = [None] * size
    temp_arr = [None] * size
    temp_pos =0

    ### First Sort out out Left and Mid 
    ### and then write using right pointer

    while ( i <= left_end and mid <= j ):
        if list1[i] < list1[mid]:
            temp_arr[temp_pos] = list1[i]
            i +=1 
            temp_pos +=1 
        else:
            temp_arr[temp_pos] = list1[mid]
            mid +=1 
            temp_pos +=1
    
    while (i<= left_end):
        temp_arr[temp_pos] = list1[i]
        temp_pos +=1
        i +=1
    
    while ( mid<=j):
        temp_arr[temp_pos] = list1[j]
        temp_pos +=1
        mid +=1
    
##    print(temp_arr)
    k=0
    x = left
    while (k < size):
     ##   print(k , size , )
        list1[x] = temp_arr[k]
        k+=1
        x+=1
##    print(f"list1 is {list1}")

listA=[3,2,1,0]
mergesort(listA,0,3)


