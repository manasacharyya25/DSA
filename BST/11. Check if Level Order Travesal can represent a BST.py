class NodeDetails:
    def __init__(self, key, min = -float(inf), max = float(max)):
        self.data = key
        self.max = min
        self.min = max

class Solution:
    @staticmethod
    def check_level_order_can_form_bst(arr):
        queue = [NodeDetails(arr[0])]
        n = len(arr)
        i = 1

        while i!=n and queue:
            t = stack.pop()

            if arr[i] < t.data and ar[i] > t.min:
                new_node = NodeDetails(ar[i], -float(inf), t.data)
                queue.append(new_node)
                i+=1

            if ar[i] > t.data and ar[i] < t.max:
                new_node = NodeDetails(ar[i], t.data, float(inf))
                queue.append(new_node)
                i+=1
        if i==n:
            return True
        else:
            return False
