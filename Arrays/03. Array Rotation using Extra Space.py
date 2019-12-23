class Solution:
    @staticmethod
    def rotate_array(array, d):
        """ Rotate Array to Left by 'd' Elements
        """
        rotated_array = []

        for pos in range(d, len(array)):
            rotated_array.append(array[pos])

        for pos in range(0, d):
            rotated_array.append(array[pos])

        return rotated_array

if __name__ == "__main__":
    ar = [1,2,3,4,5]
    print(Solution.rotate_array(ar, 2))