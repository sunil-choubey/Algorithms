##### Select a number it could be from anywhere in the data set. Pivot 
##### We will o two hand pointer , right and left , 
##### Compare the data with Pivot if the data is greater than it should lie in the right of the current data
##### If it is less than it should lie to the left of the pivot
##### Keep moing left pointer till left alue is less than Pivot
##### Keep Moving right pointer till right value > pivot value
##### if left > pivot and right < pivot then swap 
#####if right < left , The right is the partition point
##### Swap the value from left to right


def quicksort(list1,low,high):
    pivot =0
    if ( high > low):
        pivot= partition_point(list1,low,high) ##### First Pivot point
        print(pivot)
        quicksort(list1,low,pivot-1)
        quicksort(list1,pivot+1,high)


def partition_point(list1,low,high):
    print(list1,low,high)
    pivot = list1[low]
    start = low
    end = high
    temp=0
    while ( end > start):
        while list1[start] <= pivot:
            start+=1
        while list1[end] >pivot:
            end-=1
        if end > start:
            temp = list1[end]
            list1[end] = list1[start]
            list1[start] = temp
    list1[low] = list1[end]
    list1[end] = pivot
    
    ##print(list1, start ,end )
    return end


listA=[12,15,45,18,34,23,67,7]
quicksort(listA,0,len(listA)-1)