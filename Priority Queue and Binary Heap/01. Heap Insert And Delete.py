class MinHeap:
    def __init__(self):
        self.heap: list = []

    # This is different than Heap Restoration, where Parent is compared against both its children
    def heap_restoration(self, arr, i):
        """ Heap Restoration Contents of Arr starting at index i, moving upwards
        """
        while i > 0:
            parent = (i-1)//2
            # Check if Min Property is Not Satisfied at ith index
            if arr[i] < arr[parent]:
                # Swap ith element with parent element, so that Min Property is satisfied at ith index
                arr[i], arr[parent] = arr[parent], arr[i]
                # Change i to parent, and loop to check Min Property at Parent
                i = parent
            else:
                # If Min Property is satisfied at ith index, Break loop
                break

    def insert(self, k):
        self.heap.append(k)

        l = len(self.heap) - 1

        self.heap_restoration(self.heap, l)

    def print_heap(self):
        for x in self.heap:
            print(x, end=" ")
        print()


if __name__ == "__main__":
    h = MinHeap()

    h.insert(3)
    h.insert(2)
    h.insert(1)
    h.insert(5)

    h.print_heap()
