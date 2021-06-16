class Solution:
    @staticmethod
    def min_heapify(arr, i, n):
        while i < n:
            l = 2*i+1
            r = 2*i+2

            min_ind = i

            if l < n and arr[l] < arr[i]:
                min_ind = l
            if r < n and arr[r] < arr[min_ind]:
                min_ind = r

            if min_ind != i:
                arr[min_ind], arr[i] = arr[i], arr[min_ind]
                i = min_ind
            else:
                break
        return arr

    @staticmethod
    def build_heap(arr):
        n = len(arr)

        p = (n-1)//2

        while p >= 0:
            arr = Solution.min_heapify(arr, p, n)
            p -= 1

        return arr

    @staticmethod
    def kth_smallest(arr, k):
        arr = Solution.build_heap(arr)
        n = len(arr) - 1

        for i in range(k):
            arr[0], arr[n-i] = arr[n-i], arr[0]
            arr = Solution.min_heapify(arr, 0, n-i)

        print(arr[n-k+1])


if __name__ == "__main__":
    arr = [1, 4, 24, 6, 10, 0, 3]

    Solution.kth_smallest(arr, 3)
