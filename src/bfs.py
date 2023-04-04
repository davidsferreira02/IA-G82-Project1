from treenode import TreeNode



class bfs:

  def bfs(root: TreeNode, goal: TreeNode):
    queue = []
    queue.append(root)
    visited = [root.state]

    while queue:
        curr_node = queue.pop(0)
        
        if curr_node.state == goal.state:
            return curr_node
        curr_node.create_children()
        
        for child in curr_node.children:
            if child.state not in visited:
                
                
                visited.append(child.state)
                queue.append(child)
    return None