class Stack:
    def __init__(self):
        self.s = []
        self.size = 0

    def Push(self, x):
        self.size += 1
        self.s.append(x)

    def Pop(self):
        if self.size == 0:
            return -1
        top =  self.s.pop(-1)
        self.size -= 1
        return top

    def PushBack(self, x):
        if not self.s:
            self.Push(x)
        
        top = self.Pop()
        self.PushBack(x)
        self.Push(top)

    def PrintElements(self):
        for x in self.s:
            print("| ", x, " |")
        print("-------")

if __name__ == "__main__":
    stack = Stack()


    stack.Push(1)
    # stack.Push(2)
    # stack.Push(3)
    # stack.Push(4)
    stack.PushBack(0)

    stack.PrintElements()

        


