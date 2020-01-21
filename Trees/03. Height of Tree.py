class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def height_of_tree(root):
		end = "x"
		queue = [root, end]
		size = -1
		
		while queue:
			top = queue.pop(0)
			
			if top == end:
				size += 1
				if queue:
					queue.append(end)
				continue
				
			if top.left:
				queue.append(top.left)
				
			if top.right:
				queue.append(top.right)