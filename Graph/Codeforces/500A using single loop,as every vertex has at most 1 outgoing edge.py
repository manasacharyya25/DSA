if __name__=="__main__":
    is_reachable = False

    nt = input().strip().split(' ')
    
    n = int(nt[0])
    t = int(nt[1])

    _arr= input().strip().split(' ')

    portal_arr = []
    for x in _arr:
        portal_arr.append(int(x))

    for i in range(len(portal_arr)):
        portal_arr[i] += (i+1)

    curr_node = 0

    while(curr_node + 1 <= t):
        curr_node = portal_arr[curr_node]

        if curr_node == t:
            is_reachable  = True
            break
            
    if is_reachable:
        print("YES")
    else:
        print("NO")
