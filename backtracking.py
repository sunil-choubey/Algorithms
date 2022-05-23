import string
def backtracking(n,k):
    finallist=[]
    outlist=[]
    list2=list(map(int,string.digits))
    sum=0
    iter=0
    def calcnew(t):
        if t > 0:
            return 0
    for i in range(1,10,1):
        sum += backtracking
        iter +=1
        outlist.append(i)
        print(outlist,iter,sum)

        if iter == k and sum == n:
            finallist.append(outlist)
            iter=0
            sum=0
            outlist=[]
            print("finallist is ",finallist)
        elif iter == k and sum !=n :
            outlist=[]
            iter=0
            sum=0
    print(sum)
    print(outlist,finallist)


backtracking(9,2)

    
