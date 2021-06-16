class Heapsort:
    @staticmethod
    def max_heapify(arr, i, n):
        while True:
            l = 2*i+1
            r = 2*i+2

            max_ind = i

            if l < n and arr[i] < arr[l]:
                max_ind = l
            if r < n and arr[max_ind] < arr[r]:
                max_ind = r

            if max_ind != i:
                arr[i], arr[max_ind] = arr[max_ind], arr[i]
                i = max_ind
            else:
                break

        return arr

    @staticmethod
    def build_heap(arr):
        n = len(arr)

        p = (n-1)//2

        while p >= 0:
            arr = Heapsort.max_heapify(arr, p, len(arr))
            p -= 1

        return arr

    def __init__(self, arr):
        arr = Heapsort.build_heap(arr)
        n = len(arr) - 1

        for i in range(n):
            arr[0], arr[n-i] = arr[n-i], arr[0]

            arr = Heapsort.max_heapify(arr, 0, n-i)

        print(arr)


if __name__ == "__main__":
    arr = [3, 5, 1, 13, 6, 4]
    Heapsort(arr)
