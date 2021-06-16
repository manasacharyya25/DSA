class MinHeap:
    @staticmethod
    def heapify(arr, i):
        """ Compare Element at I against its child
            Swap Elements to maintain Heap Property at i
            Move down to swapped location and perform same operation
        """
        s = len(arr)

        while True:
            l = 2*i + 1
            r = 2*i + 2

            min_ind = i

            if l < s and arr[i] > arr[l]:
                min_ind = l
            if r < s and arr[r] > arr[min_ind]:
                min_ind = r

            if min_ind != i:
                arr[i], arr[min_ind] = arr[min_ind], arr[i]
                i = min_ind
            else:
                break

    @staticmethod
    def build_minheap(arr):
        s = len(arr)
        p = (s-1)//2

        for i in range(p, 0, -1):
            MinHeap.heapify(arr, i)
