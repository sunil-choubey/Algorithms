# Function to create combinations
# without itertools
def n_length_combo(lst, n):
	
    if n == 0:
        return [[]]
	
    l =[]
    for i in range(0, len(lst)):
		
        m = lst[i]
        remLst = lst[i + 1:]
		
        for p in n_length_combo(remLst, n-1):
            print(p)
            l.append([m]+p)
			
    return l

# Driver code
if __name__=="__main__":
	arr ="123"
	print(n_length_combo([int(x) for x in arr], 2))
