### Just print Numbers

sum=0
def printNum(n):
    global sum
    if n==0:   ##################base case
        return 0
    return n + printNum(n-1)       ######### recursion

    ####  it can be written as n + n-1 + printNum(n-2)
    ####     n + n-1 + n-2 + printNum(n-3)

print(printNum(5))


def factorial(n):
    if n==0:
        return 1
    
    return n * factorial(n-1)

print (factorial(5))


def sumtillk(n,k):
    global sum
    if k <= 0:   ##################base case
        ##print(f"Sum is {sum}")
        return 0
    print(n,k)
    for i in range(1,n):
        ####print(i,k,k-1)
        sum= i + sumtillk(n,k-1)       ######### recursion
        print(f"Sum is {sum} and i is {i} ")
    print(f"Sum after recursion is {sum}")
    return sum

    ####  it can be written as n + n-1 + printNum(n-2)
    ####     n + n-1 + n-2 + printNum(n-3)

print(sumtillk(5,4))


