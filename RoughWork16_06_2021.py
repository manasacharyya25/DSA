import heapq

if __name__ == '__main__':
    # arr = [1, 35, 5, 2, 6, 7, 3, 33, 34, 63, 23, 4, 43]
    arr = [35, 4, 6, 33, 34, 63, 2]
    arr1 = [35, 4, 6, 33, 34, 63, 2]

    def heapify(arr, i):
        n = len(arr)
        min_ind = i

        while True:
            l = 2*i + 1
            r = 2*i + 2

            if l < n and arr[l] < arr[i]:
                min_ind = l
            if r < n and arr[r] < arr[min_ind]:
                min_ind = r

            if i != min_ind:
                arr[i], arr[min_ind] = arr[min_ind], arr[i]
                i = min_ind
            else:
                break
        return arr

    def heapify_upwards(arr, i):
        while True:
            parent = i//2

            if arr[parent] > arr[i]:
                arr[parent], arr[i] = arr[i], arr[parent]
                i = parent
            else:
                break
        return arr

    def build_heap(arr):
        mid_ind = len(arr)//2

        for i in range(mid_ind, -1, -1):
            arr = heapify(arr, i)

        return arr

    # print(build_heap(arr))
    print(arr1)
    heapq.heapify(arr1)
    print(arr1)
    arr1.append(3)
    print(arr1)

    print(heapify_upwards(arr1, len(arr1)-1))

    # while(len(arr) > 0):
    #     print(heapq.heappop(arr))
