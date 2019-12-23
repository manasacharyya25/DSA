class Solution:
    @staticmethod
    def binary_search(array, start, end, element):
        """ Returns index of element in array if found,
            else return -1
        """
        if array[start] == element:
            return start
        if array[end] == element:
            return end
        
        mid = (start + end)//2

        if array[mid] == element:
            return mid

        if element < array[mid]:
            return Solution.binary_search(array, start, mid-1, element)
        else:
            return Solution.binary_search(array, mid+1, end, element)

        return -1


        