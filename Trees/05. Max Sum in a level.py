def levels_of_tree(root):
		end = "x"
		queue = [root, end]
		curr_sum = 0
		max_sum = -inf
		
		while queue:
			top = queue.pop(0)
			
			if top == end:
				max_sum = max(max_sum, curr_sum)
				curr_sum = 0
				if queue:
					queue.append(end)
				continue
			
			curr_sum += top.data
			
			if top.left:
				queue.append(top.left)