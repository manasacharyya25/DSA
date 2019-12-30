class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

class Tree:
    @staticmethod
    def insert(root: Node, key: int):
        """ For Insertion, Perform Level Order Traversal
            Insert the new node at the first empty position
        """
        if not root:
            return Node(key)
        
        level_order_queue = [root]

        while level_order_queue:
            curr = level_order_queue.pop(0)

            if not curr.left:
                curr.left = Node(key)
                return root
            else:
                level_order_queue.append(curr.left)
            if not curr.right:
                curr.right = Node(key)
                return root
            else:
                level_order_queue.append(curr.right)

    @staticmethod
    def delete(root: Node, key: int):
        """For deletion, Replace deepest Node with the Node to be Deleted
           Delete the deepest Node
        """
        node_to_be_deleted = None
        deepest_node = None

        if not root:
            return
        
        queue = [root]
        parent = dict()

        while not queue:
            """ While level order traversing the tree, store:
                    -   node_to_be_deleted 
                    -   deepest_node
                    -   parent of each node
            """
            curr = queue.pop(0)

            if curr.data == key:
                node_to_be_deleted = curr

            if curr.left:
                queue.push(curr.left)
                parent[curr.left.data] = curr.data

            if curr.right:
                queue.push(curr.right)
                parent[curr.right.data] = curr.data
            
            if not curr.left and not curr.right:
                deepest_node = curr
        """Swap node_to_be_deleted.data with deepest_node.data
        """
        node_to_be_deleted.data = deepest_node.data

        """Make parent of deepest_node to point to None, where it was previously pointing to deepest_node
        """
        if parent[deepest_node].right.data == deepest_node.data:
           parent[deepest_node].right = None
        elif parent[deepest_node].left.data == deepest_node.data:
           parent[deepest_node].left = None



            
