def print_sorted_order(arr):
    n = len(arr)-1
    i = 0

    stack = [0]

    while True:
        while 2*i + 1 <= n:
            stack.append(2*i + 1)
            i = 2*i + 1

        if not stack:
            break

        i = stack.pop(-1)
        print(arr[i])

        if 2*i + 2 <= n:
            i = 2*i + 2
            stack.append(i)

if __name__ == "__main__":
    print_sorted_order([4,2,5,1,3])
