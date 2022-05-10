### Just print Numbers



from traceback import print_tb


def printNum(n):
    if n==0:
        return n
    print( f"I am at {n}")
    print(printNum(n-1), f"I am at {n}")
    print( f"I am at {n}")
    return n 

printNum(5)