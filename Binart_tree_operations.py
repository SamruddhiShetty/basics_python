class Node:
    def __init__(self, data):
        self.info=data
        self.left=None
        self.right=None
    def __str__(self):
        return(self.info)
        
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
                
def pre_order(root):
    if root:
        print(root.info, end=" ")
        
        pre_order(root.left)
        
        pre_order(root.right)
        
   
        
def in_order(root):
    if root:
        in_order(root.left)
        
        print(root.info, end=" ")
        
        in_order(root.right)
    return root            #root is returned here , in this program post_order wont work until in_order is completed just to show how the object is returned and recieved
        
def post_order(root):
    if root:
        post_order(root.left)
        
        post_order(root.right)
        
        print(root.info, end=" ")
        
        
 def heightOfTree(self, root):
        if root==None:
            return 0
        else:
            return max(self.heightOfTree(root.left), self.heightOfTree(root.right))+1
        
    
        
if __name__=="__main__":
    tree=Binary_tree()
    
    while True:
        print()
        print("press 1 to insert")
        print("press 2 pre-order")
        print("press 3 in-order")
        print("press 4 post-order")
        print("press 5 to exit")
        
        print("enter your choice")
        choice=int(input())
        
        if choice==1:
            print("enter the element")
            key=int(input())
            tree.create(key)
        elif choice==2:
            pre_order(tree.root)
        elif choice==3:
            tree2=in_order(tree.root)   #here object is recieved as new object of type Node with attributes info,left and right.
        elif choice==4:
            post_order(tree2)
        else:
            break
            
            
    #for all the operations        
    #time complexity=O(n)
   #space complexity=O(h)- height of the tree(recursive stack)
            
