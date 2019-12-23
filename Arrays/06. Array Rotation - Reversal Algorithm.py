class Solution:
    @staticmethod
    def reverse_array(array):
        start = 0
        end = len(array) - 1

        if start == end or end == -1:
            return array

        while start < end:
            temp = array[start]
            array[start] = array[end]
            array[end] = temp
            
            start += 1
            end -= 1
        return array
    
    @staticmethod
    def rotate_array(array, d):
        array_a = array[0:d]
        array_b = array[d:]

        array_ar = Solution.reverse_array(array_a)
        array_br = Solution.reverse_array(array_b)

        array_ar.extend(array_br)

        rotated_arr = Solution.reverse_array(array_ar)

        return rotated_arr
        
if __name__ == "__main__":
    arr = [1,2,3,4,5]
    d = 2

    print(Solution.rotate_array(arr,d))