def solve(M, costs, order):
    ans = []
    
    if(M[order] == -1):
        print("Ambiguous")
        return None
    if(M[order] == -2) :
        print("Impossible")
        return None

    while(order > 0):
        ans.append(M[order]+1)
        order -= costs[M[order]]
    
    ans.sort()
    str1 = ' '.join(str(e) for e in ans)
    print(str1)

#We will be using this matrix to contruct solutions, where the index is the value of the order, and the value holds the item's index. A value of -2 means no solution exisst for this order size. -1 means it is ambiguous because there is already another valid solution.
M = [-2 for x in range(35000)]

#The value of order size 0 is 0, since no items succesfully correspond to zero value
M[0] = 0;

n=input()

costs=input().split(' ')

costs=list(map(int, costs))

#Here is the dynammic programming array which is going to build up solutions:

for i in range(int(n)):
    #We begin by cycling through each item cost
    cost = costs[i]
    
    for j in range(30000):
       #We are cycling through total order values: 
        
        #If we know the current order value holds a valid solution, we want to...
        if(M[j] >= 0):
            #If no solution has already been found, add our new solution including the 'cost' item we are cycling through with
            if(M[j+cost] == -2):
                M[j+cost] = i
            #If a solution has already been seen, store -1 because we have found another solution!!    
            else:
                M[j+cost] = -1
        #If this order value is already ambiguous, add a new solution that must also itself be ambiguous        
        if(M[j] == -1):
            M[j+cost] = -1
    
w=input()
orders=input().split(' ')

for i in range(int(w)):
    solve(M, costs, int(orders[i]));

