# basics_python

class Node:
    def __init__(self, data):
        self.info=data
        self.left=None
        self.right=None

        
class Binary_tree:
    def __init__(self):
        self.root=None
        
    def create(self, data):
        n=Node(data)
        if self.root==None:
            self.root=n
        else:
            current=self.root
            while True:
                if current.info < n.info:
                    if current.right==None:
                        current.right=n
                        break
                    else:
                        current=current.right
                    
                elif current.info > n.info:
                    if current.left==None:
                        current.left=n
                        break
                    else:
                        current=current.left
                else:
                    break
                    
def lca(root, v1, v2):
  #Enter your code here
    if root.info<v1 and root.info<v2:
        return lca(root.right, v1, v2)
    if root.info>v1 and root.info>v2:
        return lca(root.left, v1, v2) 
    else:
        return root
    

tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

v = list(map(int, input().split()))

ans = lca(tree.root, v[0], v[1])
print (ans.info)
