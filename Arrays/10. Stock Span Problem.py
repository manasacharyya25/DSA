"""
    https://www.geeksforgeeks.org/the-stock-span-problem/
"""

    if __name__=="__main__":
    t = int(input().strip())
    
    while t>0:
        t-=1
        
        n = int(input().strip())
        
        arr = list(map(int, input().strip().split(' ')))
        
        i = 1
        span = [1 for i in range(n)]
        stack = [0]
        
        while i < n:
            if not stack or arr[i] < arr[stack[-1]]:
                stack.append(i)
                i+=1
            else:
                top = stack.pop(-1)
                if not stack:
                    span[i] = i+1
                else:
                    span[i] = i-stack[-1]
                    
        for x in span:
            print(x, end=" ")
        print()
        