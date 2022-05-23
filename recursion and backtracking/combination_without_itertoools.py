from string import digits
from functools import reduce
import operator
from typing import final
def comb(n,keysum):
    if (keysum==0):
        return [[]]
    
    templist=[]
    k=keysum
    valueslist = list(map(int,digits))[6:]
    print("valueslist is " , valueslist)
    worklist=backtrack(valueslist,k)
    finallist =[]
    print("worklist is " , worklist, keysum)
    sum_comb=0
    for i in worklist:
        sum_comb = reduce ( operator.add, i)
        if sum_comb == n:
            finallist.append(i)
        sum_comb =0
    print(finallist)
def backtrack(list1,k):
   
    if k ==0:
        return [[]]
    templist=[]
    for i in range(0,len(list1)):
        first_elem=list1[i]
        remlist = list1[i+1:]
        print("firstelement is ",first_elem,remlist,k)
        for j in backtrack(remlist, k-1):
            templist.append([first_elem]+j)
            print("templist is ",templist, first_elem)
    
    return templist
comb(20,3)