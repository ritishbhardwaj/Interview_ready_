from TreeNodeClass import Node

ans=[]
def preorder(root:Node):
    
    if root==None:
        return
    
    # if root.left==None and root.right == None:
    #     return
        
    print(root.val)
    ans.append(root.val)
    preorder(root.left)
    preorder(root.right)
    



root = Node(val=1)
root.left=Node(val=3)
root.right=Node(val=8)
root.right.right=Node(val=6)
root.right.right.right=Node(val=5)


preorder(root)