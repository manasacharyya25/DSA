class ArrayHelper:

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


if __name__ == "__main__":
    ar = [1, 2, 3, 4, 5]
    ar_rev = ArrayHelper.reverse_array(ar)
    print(ar_rev)