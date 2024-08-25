from level_order_traversal import root
from TreeNodeClass import Node


def sol(root:Node):
    
    if root==None:
        return 0
    
    l=sol(root.left)
    r=sol(root.right)
    
    return max(l,r)+1
    
ans= sol(root)
print(ans,"Ans")