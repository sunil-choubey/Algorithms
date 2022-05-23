from itertools import combinations
from string import digits
from functools import reduce
import operator

def combination(n,k):
    if n<=0:
        return 0
    
    sum_data=0
    finallist = []
    newarr = list(map(int,digits))
    newarr.pop(newarr.index(0))
    newlist=list(combinations(newarr,k))
    print(newlist, len(newlist))

    for i in newlist:
        sum_data = reduce(operator.add,i)
        print(sum_data)
        if sum_data== n:
            finallist.append(list(i))
        sum_data=0

    print(finallist)

combination(20,4)
    