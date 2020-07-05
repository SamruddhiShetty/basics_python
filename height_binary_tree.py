# basics_python

#maximum height or depth of binary tree

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
                    
def height(root):
    if root==None:
        return -1
    else:
        return(max(height(root.left), height(root.right)) +1)
                    
if __name__=="__main__":
    tree1=Binary_tree()
    while True:
        print("press 1 to insert")
        print("press 2 to find the height")
        print("press 3 to exit")
        
        print("enter your choice")
        choice=int(input())
        
        if choice==1:
            print("enter the value")
            value=int(input())
            tree1.create(value)
        elif choice==2:
            print(height(tree1.root))
        else:
            break
