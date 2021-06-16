
class Solution:
    @staticmethod
    def findLongestConseqSubseq(arr):
        mx = max(arr)
        mn = min(arr)

        hash_arr = [0 for i in range(mx+1)]

        curr_max = float("-inf")

        for i in range(len(arr)):
            hash_arr[arr[i]] = hash_arr[arr[i]-1]+1
            curr_max = max(curr_max, hash_arr[arr[i]])

        return curr_max


if __name__ == '__main__':
    print(Solution.findLongestConseqSubseq([2, 6, 1, 9, 4, 5, 3]))
