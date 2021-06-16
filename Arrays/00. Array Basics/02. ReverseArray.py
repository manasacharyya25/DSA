class Solution:
    @staticmethod
    def reverseList(A, start, end):
        while start < end:
            A[start], A[end] = A[end], A[start]
            start += 1
            end -= 1
        return A


if __name__ == '__main__':
    print(Solution.reverseList([1, 2, 4, 5, 6, 7], 0, 3))
    print(Solution.reverseList([1, 2, 4, 5, 6, 7], 3, 5))
