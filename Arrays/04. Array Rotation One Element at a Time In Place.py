class Solution:
    @staticmethod
    def rotate_array(array, d):
        while d>0:
            d -= 1
            temp = array[0]
            for pos in range(len(array)-1):
                array[pos] = array[pos+1]
            array[pos+1] = temp
            print(array)

if __name__=="__main__":
    ar = [1,2,3,4,5]
    d = 2
    Solution.rotate_array(ar, d)