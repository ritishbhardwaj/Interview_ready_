from TreeNodeClass import Node


d = {}
maxi = -100000000
def sol(root:Node,lvl):
    global maxi
    
    if root==None:
        return
    
    maxi = max(maxi,lvl)
    if lvl not in d:
        d[lvl] = [root.val]
    else:
        d[lvl].append(root.val)
    
    sol(root.left,lvl+1)
    sol(root.right,lvl+1)
    




root=Node(val=3)
root.left = Node(val=9)
root.right=Node(val=20)
root.right.right=Node(val=7)
root.right.left=Node(val=15)

if __name__ == "__main__":
    print(sol(root,lvl=0))
    print(d,maxi+1)