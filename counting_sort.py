####  We identify what value is greater than a particular value
####  and place the value at the given location in the new array

#### Idea is to create an array data structure that keep the count of each number
#### Now just add all the previos items n-1 + n 
#### Then populate the new sorted array based on the position


### Consider the example as 
#### Arraya Input = 5,4,7,2,5
#### First Thing to do is create an array of size maxsize + 1 --> 7+1 and populate 0 in it  , 1 is just a constant number and you can choose any number
#### Array Temp = 0 0 0 0 0 0 0 0 0
#### Now Populate the corresponding position with 1 and if there is a repetion as in our case 5 is repeated add 1 to that position
#### Array Temp = 0 0 1 0 1 2 0 1 0 
#### Add n-1 element value to nth element in temp array
#### Array Temp = 0 0 1 1 2 4 4 5 5
#### Population of Final Output
#### Read the Input arraya Element and search the value of the Element in temp array , For Example first element is 5 in in put array, 
#       Value of the element 5  in teparray is 4 , So we need to populate in Last array at position 3  and reduce 1 from that element position
#       Just showing how the Final list wil look like after each iteration
####    1st Iteration Final Output = _ _ _ 5 _                  Arraya temp = 0 0 1 1 2 3 4 5 5
####    2nd Iteration Final Output = _ 4 _ 5 _                  Arraya temp = 0 0 1 1 1 3 4 5 5
####    3rd Iteration Final Output = _ 4 _ 5 7                  Arraya temp = 0 0 1 1 1 3 4 4 5
####    4th Iteration Final Output = 2 4 _ 5 7                  Arraya temp = 0 0 0 1 1 3 4 5 5
####    5th Iteration Final Output = 2 4 5 5 7                  Arraya temp = 0 0 0 1 1 2 4 5 5

from re import template
def def_value():
    return 0
def counting_sort(list1):
    ll = len(list1)
    max_value = max(list1) 
    templist=[0]* ( max_value  + 10)
    ###print(len(templist))
    finallist=[0]*ll
    for i in list1:
        templist[i] +=1
    ###print(templist)

    for j in range(1,len(templist)):
        templist[j] = templist[j] + templist[j-1]
    ##print(templist)    
    for k in range(len(finallist)):
        print(k, templist[list1[k]])
        finallist[templist[list1[k]] - 1] = list1[k]
        templist[list1[k]] -=1
    
    ###print(finallist)

listA = [19,7,45,23,7,0]
counting_sort(listA)